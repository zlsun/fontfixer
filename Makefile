
all: fontfixer.css
	@xclip -sel c $<
	@cat $<

clean:
	$(RM) fontfixer.css

rebuild:
	make --no-print-directory clean
	make --no-print-directory

fontfixer.css: fontfixer.py
	python $< > $@

