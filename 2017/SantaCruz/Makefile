PALESTRAS=opencv_python linux_distros

%.pdf: %.tex
	pdflatex $<
	pdflatex $<
	$(RM) *.aux *.dvi *.out *.log *.nav *.snm *.toc

all: $(patsubst %,%.pdf,$(PALESTRAS))

.PHONY: all clean

clean:
	$(RM) *.aux *.dvi *.pdf *.out *.log *.nav *.snm *.toc
