---
title: "Mathematical insights and difficulties in spatial population genetics"
author: "Peter Ralph <br/> University of Oregon <br/> Dept of Data Science"
date: "BartonFest '25<br/> IST // 26 August 2025"
---

--------------------

<!--
title-slide-attributes:
    data-background-image: /path/to/title_image.png
    data-background-size: contain
-->

> UO is located on the traditional indigenous homeland of the Kalapuya people.
Kalapuya people were dispossessed of their indigenous homeland by the United States government and forcibly removed.
Today, Kalapuya descendants are primarily citizens of the Confederated Tribes of Grand Ronde and the Confederated Tribes of Siletz Indians,
and continue to make important contributions to their communities, to the UO, to Oregon, and to the world.


## 

::: {.columns}
:::::: {.column}

**Joint work with:**

- Alison Etheridge (Oxford)
- Tom Kurtz (Madison)
- Ian Letter (ex-Oxford)
- Terence Tsui (Warwick)

:::
:::::: {.column width=50%}

![](figs/coauthors.png)

:::
::::::


*slides:* [github.com/petrelharp/barton-2025](https://petrelharp.github.io/barton-2025/barton-2025.slides.html)


# First, some thanks


## {data-background-image="figs/dynamics-of-hybrid-zones.png" data-background-position=center data-background-size=100%}

## {data-background-image="figs/bde.png" data-background-position=center data-background-size=100%}

## Thanks, Nick!!

<!--
Intro to the problem
-->

# {data-background-image="figs/popgen-in-space-new.jpeg" data-background-position=center data-background-size=100%}

::: {.caption .bottomright}
'art' by G. Coop
:::

##

![](figs/ibd-by-some-pops.png)

::: {.caption}
Desert tortoises, courtesy Brad Shaffer and Evan McCartney-Melstad
:::

## 

![](figs/within-ivanpah-ibd.png)

::: {.caption .bottomright}
Desert tortoises, courtesy Brad Shaffer and Evan McCartney-Melstad
:::

<!--
The population model
-->

# Spatial populations {data-background-image="sims/slim_density_anim.gif" data-background-position=center data-background-size=100%}


## A model {data-background-image="figs/model.png" data-background-position=center data-background-size=100%}

::: {.columns}
:::::: {.column width=50%}

Every individual:

::: incremental
- reproduces at rate <span class="red">$\gamma$</span>
- dies at rate <span class="blue">$\mu$</span>
:::

::: fragment
Offspring:

::::: incremental
- disperse with variance <span class="yellow">$\sigma^2$</span>
- establish with probability <span class="red">$r$</span>
:::::
:::

::: fragment
All this can depend on *location* and *local density*,
measured with a kernel $\rho$:
$$\text{(density at $x$)} = \sum_i \rho(x_i - x).$$
:::

::::::
:::::: {.column width=50%}

::::::
:::

## {data-background-image="figs/forwards-and-backwards.png" data-background-position=center data-background-size=100%}

::: red
Everything here is thanks to Tom Kurtz,

who showed us how to do it.
:::

::: r-stretch

:::

---------

![](sims/expansion.pop.mp4)


## Population dynamics {data-background-image="figs/model.png" data-background-position=right data-background-size=75%}

::: {.columns}
:::::: {.column width=50%}

The population density $\varphi_t(x)$ at time $t$
(*number* of individuals is $N\varphi(x)$)

::: fragment
changes because of <span class="yellow">*migration*</span>
$$\begin{aligned}
    \frac{d}{dt} \varphi_t(x)
    &=
    r(x) \frac{1}{2\sigma^2} \Delta (\gamma \varphi_t)(x) \color{white}{+ \varphi_t(x) F(x)}
\end{aligned}$$
:::

::: fragment
and *<span class="red">reproduction</span>/<span class="blue">death</span>*:
$$\begin{aligned}
    \frac{d}{dt} \varphi_t(x)
    &=
    r(x) \frac{1}{2\sigma^2} \Delta (\gamma \varphi_t)(x) + \varphi_t(x) F(x) ,
\end{aligned}$$
where
$F(x) = r(x) \gamma(x) - \mu(x)$
:::

::::::
:::::: {.column width=50%}

::::::
:::

## Forwards: lines of descent {data-background-image="figs/model.png" data-background-position=right data-background-size=75%}

::: {.columns}
:::::: {.column width=50%}

A *potential* line of descent $Y_t$
diffuses at rate $\sigma^2 \gamma(x)$:
$$dY_t = \sigma^2 \gamma(Y_t) dB_t .$$

::: fragment
The density of *successful* lines of descent
:::
::: fragment
from location $x$ at time $s$ to location $y$ at time $t$
is $h_{s,t}(x,y)$, where
$$\int h_{s,t}(x,y) f(y) dy = \mathbb{E}_x[f(Y_t) e^{-\int_s^t b(Y_u) du}],$$
:::

::: fragment
and
$$\begin{aligned}
    b(x)
    &= \text{(mean net reproductive output at $x$)} \\
    &= \gamma(x) \int r(y) q(x,dy) - \mu(x) .
\end{aligned}$$
:::


::::::
:::::: {.column width=50%}

::::::
:::

## Consistency {data-background-image="figs/model.png" data-background-position=right data-background-size=75%}

::: {.columns}
:::::: {.column width=50%}
The kernel $h_{s,t}(x,y)$ defined by
$$\int h_{s,t}(x,y) f(y) dy = \mathbb{E}_x[f(Y_t) e^{-\int_s^t b(Y_u) du}],$$

is what evolves the density forwards in time:
$$\varphi_t(y) = \int \varphi_s(x) h_{s,t}(x,y) dx .$$

::::::
:::::: {.column width=50%}

::::::
:::



---------

![](sims/expansion.lineages.mp4)

## Backwards: lineages {data-background-image="figs/model.png" data-background-position=right data-background-size=75%}

::: {.columns}
:::::: {.column width=65%}


Suppose population has a stationary density $\varphi(x)$. Then
$$ dL_t = r(L_t) \gamma(L_t) 2 \nabla \log(\varphi\gamma)(L_t) dt
+ \sqrt{r(L_t)\gamma(L_t)} dB_t$$


::: incremental
- Lineage speed determined by rate of production of mature offspring
    (<span class="red">$r\gamma$</span>, $\approx$ death),
- and drawn to regions of high total fecundity
    (<span class="red">$\varphi \gamma$</span>).
- Reversible with respect to
$$\color{red}{\pi(x) = \frac{\gamma(x,\varphi(x)) w(x)^2 }{ r(x,w(x))}.} $$
:::

::::::
:::::: {.column width=50%}

::::::
:::


## What about branching? {data-background-image="figs/model.png" data-background-position=right data-background-size=75%}

::: {.columns}
:::::: {.column width=50%}


Successful lines of descent *branch*
at rate
$$\begin{aligned}
    \frac{1}{N} c(x) 
    &= \frac{1}{N} \text{(total birth + death rate)} \\
    &= \frac{1}{N} \left( \gamma(x) \int r(y) q(x,dy) + \mu(x) \right)
\end{aligned}$$

::: fragment
and so the density of *close relatives*
at locations $x$ and $y$ and time $t$
from time $s$ is
$$\begin{aligned}
    \frac{1}{N} \int \varphi_s(z) c(z) h_{s,t}(z,x) h_{s,t}(z,y) dz .
\end{aligned}$$
:::

::::::
:::::: {.column width=50%}

::::::
:::

## Can we *use* this? {data-background-image="sims/slim_density_screenshot_inverted.png" data-background-position=center data-background-size=100%}

::: {.columns}
:::::: {.column width=50%}

<!--
![](sims/bde/out_123.locs.png)
-->

::::::
:::::: {.column width=50%}

![](sims/bde/out_123.ibd.png)

::::::
:::


<!--
Close relatives
-->

# Close relatives

## 

![](figs/barton-wilson-header.png)

::: {.columns}
:::::: {.column width=50%}

![](figs/barton-wilson-ARGs_hl.png)

::::::
:::::: {.column width=50%}


![](figs/barton-wilson-close-rels1_hl.png)

::::::
:::

##

Suppose that we've sampled $K$ individuals
with intensity $\nu(x)$
and observed close relatives $\{(x_i, y_i, t_i)\}_{i=1}^P$,
with locations $(x_i, y_i)$ and TMRCAs $t_i$ ago.

How many such pairs do we *expect* to see?

Well, the intensity of such pairs is
$$\begin{aligned}
w(x,y,t) = \int \varphi_{-t_i}(z) c(z) h_{-t,0}(z,x) h_{-t,0}(z,y)
\end{aligned}$$
and so the expected number with $s \le t_i \le t$ is
$$
\frac{K^2}{N} \int_s^t w(x,y,u) \nu(x) \nu(y) dx dy du .
$$

## Does it work?

*Simulation:* pairs with an ancestor within 20 generations
iin 100 samples from a spatial population
with a total of $10^4$:

::::: r-stack

::: {.fragment .coverup}
![](figs/sim_pairs_1.png)
:::

::: {.fragment .coverup}
![](figs/sim_pairs_1_2.png)
:::

::: {.fragment .coverup}
![](figs/sim_pairs_1_2_3.png)
:::

:::::


# Wrap-up

## Spatial population genetics?

Moving forwards:

::: incremental
- A likelihood-based way to fit spatially
    heterogeneous population models?
- More theory needed for patchy/stochastic populations!
- S(L)imulation: see [Chevy et al, *A Guide to Individual-Based Simulations in Continuous Landscapes*](https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.71098)
:::

. . .

**Thanks** to Nick, Alison, and Tom

## {data-background-image="figs/guillemots_thanks.png" data-background-position=center data-background-size=50%}



<!--
Wright-Malécot
-->

# Other stuff

## Wright (1943), Malécot (1948)

If the population at time $t$ has density $\varphi_t(x)$,
so that the *number* near $x$ is $N \varphi_t(x)$,
and

$$ I_t(x,y) = (\text{proportion identity between $x$ and $y$ at time $t$}) , $$

then maybe
$$\begin{aligned}
    I_t(x,y)
    &=
        (1-\mu)^2 \sum_{x',y'} \varphi_{t-1}(x') \varphi_{t-1}(y') I_{t-1}(x',y') p_1(x',x) p_1(y',y)
    \\ &\qquad
        + (1-\mu)^2 \frac{1}{N} \sum_z \varphi_{t-1}(z) p_1(z,x) p_1(z,y) (1 - I_{t-1}(z,z)),
\end{aligned}$$
where dispersal is
$$ p_1(z,x) = \mathbb{P}\{\text{offspring from $z$ goes to $x$}\} . $$

::: {.caption}
better explanations: XXX
:::

## Backwards

$$\begin{aligned}
    I_t(x,y)
    &=
        (1-\mu)^2 \sum_{x',y'} \varphi_{t-1}(x') \varphi_{t-1}(y') I_{t-1}(x',y') p_1(x',x) p_1(y',y)
    \\ &\qquad
        + (1-\mu)^2 \frac{1}{N} \sum_z \varphi_{t-1}(z) p_1(z,x) p_1(z,y) (1 - I_{t-1}(z,z))
\end{aligned}$$

Two individuals today are identical if

- their parents were distinct and identical
- or they are siblings,
- and neither got a new mutation.


## Forwards

$$\begin{aligned}
    I_{t+1}(x,y)
    &=(1-\mu)^2 \sum_{x',y'} \varphi_{t}(x') \varphi_{t}(y') I_{t}(x',y') p_1(x',x) p_1(y',y)
    \\ &\qquad
        + (1-\mu)^2 \frac{1}{N} \sum_z \varphi_{t}(z) p_1(z,x) p_1(z,y) (1 - I_{t}(z,z))
\end{aligned}$$

In the next generation, those who are identical

- have distinct and identical parents,
- or are siblings,
- except for when new mutation intevenes.


## A solution

At stationary, and in continuous time,
we get
$$\begin{aligned}
    \frac{\sigma^2}{2} (\Delta_x + \Delta_y) I_t(x,y) - 2 \mu I(x,y)
    &= - \frac{1}{N} \delta_0(x-y) (1 - I(x,y)) .
\end{aligned}$$

The solution is
$$\begin{aligned}
    \frac{I(x,y)}{1 - I(XXX)}
    &= \frac{1}{N} \int_0^\infty \int e^{-2 \mu t} \varphi_t(z) p_t(z,x) p_t(z,y) dz dt .
\end{aligned}$$

Interpretation: sum over all coalescence times.

Solution, in $\mathbb{R}^2$:
$$ I(x,y) = K_0(xyz) . $$

:tada:


<!--
Difficulties
-->

## Difficulties

1. What is $N$?
2. Um but $K_0(0) = \infty$?
3. Offspring don't move independently, especially successful ones.


## What's really going on?

Let $\tau_{xy}$ be the TMRCA of samples at $x$ and $y$,
so that $I(x,y) = \mathbb{E}[e^{-2\mu t} \tau_{xy}]$,

and
$$\begin{aligned}
     n_s(z;x,y) &= (\text{number of pairs at $x,y$} \\
            &\qquad \text{whose MRCA is at $z$, time $s$ ago}) .
\end{aligned}$$

Then
$$\begin{aligned}
    \mathbb{P}\{ \tau_{xy} \le t \}
    = \frac{ \int_0^t \int n_s(z;x,y) dz ds }
           { \int_0^\infty \int n_s(z;x,y) dz ds } .
\end{aligned}$$

We want
$$ n_s(z;x,y) = C p_s(z,x) p_s(z,y) , $$
with $C$ a constant (local birth rate).

## The problem

We want

1. $n_s(z;x,y) = C p_s(z,x) p_s(z,y)$, with $C$ a constant, and
2. $\int_0^\infty \int n_s(z;x,y) dz ds < \infty$.

. . .

[EKLRT](https://dx.doi.org/10.1214/24-EJP1075)
showed that these are contradictory*.

More generally: continuous spatial population models* can either have

1. finite coalescent time distributions, or
2. be deterministic,

but not both.

. . .

::: {.caption}
*${}^*$some terms and conditions may apply*
:::

## Open question

There is nonetheless an expression for $I$ in $d=1$;
how do you get this out of the 
[EKLRT](https://dx.doi.org/10.1214/24-EJP1075) model?

