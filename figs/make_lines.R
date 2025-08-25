# Note that (because of plotting)
# that time is "time ago" here.

nize <- function (x) { (cumsum(x)[-length(x)] / sum(x) )|> round(6) }

make_grid <- function (n, t) {
    xy <- do.call(rbind, lapply(1:t, function (s) {
        cbind(x=nize(rgamma(rpois(1, n)+2, shape=6)), t=s)
    })) |> data.frame()
    return(xy)
}

make_parents <- function(xy) {
    pc <- do.call(rbind, lapply(unique(xy$t)[-1], function (t) {
        cx <- xy$x[xy$t == t-1]
        px <- xy$x[xy$t == t]
        cbind(
              px=sort(sample(px, size=length(cx), replace=TRUE)),
              pt=t,
              cx=cx,
              ct=t-1
        )
    })) |> data.frame()
}

trace_up <- function (t, k, pc) {
    x <- pc$cx[pc$ct == t][k]
    out <- data.frame(x=x, t=t)
    while (t <= max(pc$ct)) {
        k <- which(pc$ct == t & pc$cx == x)
        x <- pc$px[k]
        t <- pc$pt[k]
        out <- rbind(out, data.frame(x=x, t=t))
    }
    return(out)
}

go_down <- function (t, k, pc) {
    # finds the deepest descendant(s) of t, k
    j <- which(pc$ct == t)[k]
    while (length(j) > 0) {
        x <- pc$cx[j]
        t <- pc$ct[j]
        j <- which(pc$pt %in% t & pc$px %in% x)
        stopifnot(length(unique(t)) == 1)
    }
    k <- match(x, pc$cx[pc$ct == t[1]])
    return(data.frame(k=k, t=t))
}

num_descendants <- function(s, t, pc) {
    stopifnot(s < t)
    x <- subset(pc, ct==s)$cx
    n <- rep(1, length(x))
    for (u in s:(t-1)) {
        px <- subset(pc, ct==u+1)$cx
        pn <- tapply(n,
                 factor(
                    match(subset(pc, ct==u)$px, px),
                    levels=seq_along(px)),
                 sum)
        pn[is.na(pn)] <- 0
        x <- px
        n <- pn
    }
    return(n)
}

pick_branch_point <- function (t, pc) {
    x <- subset(pc, ct == t)$cx
    n <- num_descendants(1, t, pc)
    k <- sample(which(n > 1), 1)
    return(k)
}

plot_setup <- function (xy, pc) {
    layout(t(1:3))
    for (i in 1:2) plot(0, type='n', xlab='', ylab='', xaxt='n', yaxt='n', bty='n')
    plot(xy, pch=20, xaxt='n', yaxt='n', xlab='', ylab='')
    segments(x0=pc$cx, y0=pc$ct, x1=pc$px, y1=pc$pt, col='grey')
}

set.seed(123)
N <- 30
T <- 30
xy <- make_grid(N, T)
pc <- make_parents(xy)
n <- table(xy$t)

png(file="lines_potential.png", width=1500, height=1000, pointsize=10)
    plot_setup(xy, pc)
    lines(trace_up(14, floor(n[14]/2), pc), col='blue', lwd=2)
    lines(trace_up(6, floor(2*n[6]/3), pc), col='blue', lwd=2)
dev.off()

# successful
png(file="lines_successful.png", width=1500, height=1000, pointsize=10)
    plot_setup(xy, pc)
    lines(trace_up(14, floor(n[14]/2), pc), col='blue', lwd=2)
    lines(trace_up(6, floor(2*n[6]/3), pc), col='blue', lwd=2)
    lines(trace_up(1, floor(n[1]/2), pc), col='red', lwd=2)
dev.off()

# all successful
png(file="lines_successful_all.png", width=1500, height=1000, pointsize=10)
    plot_setup(xy, pc)
    # all of them
    for (k in 1:n[1]) {
        lines(trace_up(1, k, pc), col='red', lwd=2)
    }
dev.off()

# lineage
png(file="lines_lineage.png", width=1500, height=1000, pointsize=10)
    plot_setup(xy, pc)
    lines(trace_up(1, floor(n[1]/2), pc), col='red', lwd=2)
dev.off()

# branching
png(file="lines_branching.png", width=1500, height=1000, pointsize=10)
    plot_setup(xy, pc)
    t <- T-10
    bk <- pick_branch_point(t, pc)
    kk <- go_down(t, bk, pc)$k
    for (k in c(min(kk), max(kk))) {
        lines(trace_up(1, k, pc), col='red', lwd=2)
    }
dev.off()


## rare branching
N <- 900
T <- 30
xy <- make_grid(N, T)
pc <- make_parents(xy)
n <- table(xy$t)


# branching
png(file="lines_branching_rare.png", width=1500, height=1000, pointsize=10)
    plot_setup(xy, pc)
    t <- T-10
    bk <- pick_branch_point(t, pc)
    kk <- go_down(t, bk, pc)$k
    for (k in c(min(kk), max(kk))) {
        lines(trace_up(1, k, pc), col='red', lwd=2)
    }
dev.off()

# all successful
png(file="lines_successful_all_rare.png", width=1500, height=1000, pointsize=10)
    plot_setup(xy, pc)
    # all of them
    for (k in 1:n[1]) {
        lines(trace_up(1, k, pc), col='red', lwd=2)
    }
dev.off()

