.PHONY : all

all : model.png sim_pairs_1.png sim_pairs_1_2.png sim_pairs_1_2_3.png

sim_pairs_%.pdf : sim_pairs.ink.svg
	./export-layers-svg.sh $< $@ $(subst _, ,$*)

include ../rules.mk
