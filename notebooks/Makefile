# dependencies
# (*) for the sphinx engine (readthedocs)
#     pip install ipypublish[sphinx]
# (*) fore cleaning things up (only locally for profs)
#     pip install nbstripout

all: book
clean: book-clean
view: book-open

.PHONY: book book-clean book-open

book:
	jupyter-book build .

book-clean:
	rm -rf _build

# warning: convenience, works on mac only
book-open:
	open _build/html/index.html
