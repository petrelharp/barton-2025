all : \
	bde/out_123.ibd.png \
	bde/out_123.locs.png \
	bde_hd/out_123.locs.png \
	bde_hd/out_123.ibd.png

# don't delete intermediate files
.SECONDARY :

%.ibd.png : %.json
	python plot_ibd.py $<

%.locs.png : %.trees
	python plot_locations.py $<

%.json : %.trees
	python compute_stats.py $<

1d/out_%.trees : 1d.slim
	slim -s $* -d 'OUTDIR="1d"' $<

bde/out_%.trees : bde.slim
	slim -s $* -d 'OUTDIR="bde"' $<

bde_hd/out_%.trees : bde_high_density.slim
	slim -s $* -d 'OUTDIR="bde_hd"' $<
