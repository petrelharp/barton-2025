import numpy as np
import matplotlib.pyplot as plt

import tskit, pyslim


def compute_isolation_by_distance(ts, targets, indivs):
    """
    Compute mean sequence divergence of each indivs to each of the targets
    """
    all_indivs = np.concatenate([targets, indivs])
    num_targets = len(targets)
    div = ts.divergence(
            sample_sets = [ts.individual(ind).nodes for ind in all_indivs],
            indexes = [(i, j) for i in range(len(targets), len(all_indivs))
                              for j in range(len(targets))],
            mode='branch'
    )
    div.shape = (len(indivs), len(targets))
    return div


def plot_isolation_by_distance(indiv_locs, target_locs, div, figsize, xlim=None, mu=1e-6):
    """
    Note this plots probability of identity, not genetic distance!
    """
    dists = np.sqrt(
                np.power(indiv_locs[:, 0, np.newaxis] - target_locs[:, 0].T, 2)
                + np.power(indiv_locs[:, 1, np.newaxis] - target_locs[:, 1].T, 2)
    )
    ibd = np.exp(-mu * div)
    num_targets = div.shape[1]
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    for k in range(num_targets):
        ax.scatter(dists[:, k],
                   ibd[:, k],
                   s = 20, 
                   alpha = 0.75,
                   edgecolors = 'none',
        )
    # add a line
    # bins = np.linspace(0, np.max(dists) + 5, 12)
    bins = np.quantile(dists.flatten() * 1.01,
                       np.linspace(0, 1, 21))
    bins[0] = 0.0
    whichbin = np.digitize(dists, bins) - 1
    n = np.bincount(
            whichbin.flatten(),
            minlength=len(bins)-1,
    )
    mean_ibd = np.bincount(
            whichbin.flatten(),
            weights=ibd.flatten(),
            minlength=len(bins)-1,
    )
    ut = (n > 10)
    mean_ibd = mean_ibd[ut] / n[ut]
    n = n[ut]
    mids = (bins[1:] - np.diff(bins)/2)[ut]
    ax.plot(mids, mean_ibd)
    if xlim is not None:
        ax.set_xlim(0, xlim)
    ax.set_xlabel("geographic distance")
    ax.set_ylabel("P(IBD)")
    return fig

