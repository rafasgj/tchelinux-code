PALESTRAS=pygame fotografia

# LATEX=latex
LATEX=xelatex

%.pdf: %.tex
	$(LATEX) $<
	$(LATEX) $<
	$(RM) *.aux *.dvi *.out *.log *.nav *.snm *.toc *.vrb *.xdv

all: $(patsubst %,%.pdf,$(PALESTRAS))

.PHONY: all clean

clean:
	$(RM) *.aux *.dvi *.pdf *.out *.log *.nav *.snm *.toc *.fls *.fdb_latexmk *.synctex.gz *.vrb *.xdv
