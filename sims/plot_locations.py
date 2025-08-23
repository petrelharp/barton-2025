#!/usr/bin/env python3

import sys
import tskit, pyslim
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

if len(sys.argv) == 1:
    raise ValueError("Usage:  plot_locations.py [treefile [treefile]]")

treefiles = sys.argv[1:]

for treefile in treefiles:
    print(treefile)
    outfile = ".".join(treefile.rsplit(".")[:-1] + ["locs", "png"])
    ts = tskit.load(treefile).simplify()
    inds = ts.individuals_flags & pyslim.INDIVIDUAL_ALIVE > 0
    locs = ts.individuals_location[inds,:]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, ts.metadata['SLiM']['user_metadata']['WIDTH'][0])
    ax.set_ylim(0, ts.metadata['SLiM']['user_metadata']['HEIGHT'][0])
    ax.set_aspect('equal')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    pts = ax.scatter(locs[:,0], locs[:,1], s=5, c="black")
    fig.set_size_inches([3,3])
    plt.savefig(outfile, dpi=288)
    print("---> ", outfile)

print("... done!")

