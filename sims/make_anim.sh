#!/bin/bash

# To run this I took a bunch of screenshots of the SLiMgui
# and put them in the directory `anim/`.

set -eo pipefail

magick -size 2256x1504 -delay 20 -loop 0 anim/*.png temp.gif
convert temp.gif -channel RGB -negate slim_density_anim.gif
rm temp.gif
