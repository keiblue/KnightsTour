# KnightsTour.py makeFile

file = KnightsTour.py
.SILENT:

view: $(file)
	cat $(file) | less
run: $(file)
	python $(file) $$KNIGHT_ROWS $$KNIGHT_COLS $$KNIGHT_ATTS

.PHONY : clean
clean:
	- \rm *.pyc
