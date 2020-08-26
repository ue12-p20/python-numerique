%.yamlb: stem=$(subst .yamlb,,$@)
%.yamlb: %.yaml
	openssl base64 -in $(stem).yaml -out $@ 

ALL=$(shell git ls-files *.yamlb)

all: $(ALL)