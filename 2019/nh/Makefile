PALESTRAS=pygame fotografia buildroot

# LATEX=latex
LATEX=xelatex

%.pdf: %.key
	keynotec $<

%.pdf: %.tex
	TEXINPUTS=${TEXINPUTS}:../.. $(LATEX) $<
	TEXINPUTS=${TEXINPUTS}:../.. $(LATEX) $<
	$(RM) *.aux *.dvi *.out *.log *.nav *.snm *.toc *.vrb *.xdv

all: $(patsubst %,%.pdf,$(PALESTRAS))

.PHONY: all clean

clean:
	$(RM) *.aux *.dvi *.pdf *.out *.log *.nav *.snm *.toc *.fls *.fdb_latexmk *.synctex.gz *.vrb *.xdv
