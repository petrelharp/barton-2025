#!/usr/bin/env python3

import sys, os
import json
import numpy as np
import matplotlib.pyplot as plt

import tskit, pyslim

from helpers import *

# from https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

for treefile in sys.argv[1:]:
    basename = ".".join(treefile.split(".")[:-1])
    ts = tskit.load(treefile)
    ts = pyslim.recapitate(ts, ancestral_Ne=300, recombination_rate=1e-8)

    alive = pyslim.individuals_alive_at(ts, 0)
    num_targets = 40
    num_indivs = min(40, len(alive) - num_targets)
    locs = ts.individual_locations
    targets = np.random.choice(alive, num_targets)
    other_alive_inds = np.array(list(set(alive) - set(targets)))
    indivs = list(np.random.choice(other_alive_inds, num_indivs, replace=False))

    datafile = basename + ".ibd.txt"
    if os.path.isfile(datafile):
        print(datafile, "already exists.")
        data = np.loadtxt(datafile)
        assert np.all(data[:3, :3] == -1)
        targets = data[0, 3:].astype("int")
        target_locs = data[1:3, 3:].T
        indivs = data[3:, 0].astype("int")
        indiv_locs = data[3:, 1:3]
        div = data[3:, 3:]
    else:
        print(datafile, "does not exist, computing.")
        div = compute_isolation_by_distance(ts, targets, indivs)
        target_locs = locs[targets, :2]
        indiv_locs = locs[indivs, :2]
        data = np.full((3 + len(indivs), 3 + len(targets)), -1)
        data[0, 3:] = targets
        data[1:3, 3:] = target_locs.T
        data[3:, 0] = indivs
        data[3:, 1:3] = indiv_locs
        data[3:, 3:] = div
        np.savetxt(datafile, data)

    out = {}
    out['metadata'] = ts.metadata['SLiM']
    out['diversity'] = ts.diversity(mode='branch')
    out['popsize'] = ts.num_samples / 2
    out["ibd"] = {
            "indiv_locs" : indiv_locs,
            "target_locs" : target_locs,
            "div" : div,
    }

    with open(basename + ".json", "w") as f:
        json.dump(out, f, cls=NumpyEncoder)
