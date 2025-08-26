SHELL := /bin/bash
# use bash for <( ) syntax

.PHONY : setup

TARGET := barton-2025.slides.html

$(TARGET) : setup

setup :
	$(MAKE) -C figs
	$(MAKE) -C sims

publish : $(TARGET)
	# do this after giving the talk
	sed -i '/mathjax: .*MathJax.js/d' $<

include rules.mk
