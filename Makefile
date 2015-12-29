
MAKE = make --no-print-directory

color = \e[1;31m
reset = \e[0m
header = "$(color)[$(1)]$(reset) $(2)"

all: fontfixer.css
	@cat $<
	@-xclip -sel c $<

clean:
	@echo -e $(call header,Cleanning)
	@$(RM) fontfixer.css

rebuild:
	@$(MAKE) clean
	@$(MAKE)

%.css: %.py
	@echo -e $(call header,Generating,$@)
	@python $< > $@

