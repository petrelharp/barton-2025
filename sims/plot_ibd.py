#!/usr/bin/env python3

import sys
import json
import matplotlib.pyplot as plt
import numpy as np

from helpers import *

for treefile in sys.argv[1:]:
    basename = ".".join(treefile.split(".")[:-1])
    with open(basename + ".json", 'r') as f:
        data = json.load(f)
        for x in data['ibd']:
            data['ibd'][x] = np.array(data['ibd'][x])
    xmax = data['metadata']['user_metadata']['WIDTH'][0]
    ymax = data['metadata']['user_metadata']['HEIGHT'][0]
    figsize = (6, 6 * ymax / xmax)
    fig = plot_isolation_by_distance(**data["ibd"], figsize=figsize, xlim=xmax/2)
    plt.tight_layout()
    plt.savefig(basename + ".ibd.png")
