.PHONY: man testman test up check dist

test:
	./run-tests.sh

man:
	pandoc README.rst -s -t man -o rst2jira.1

testman:
	pandoc README.rst -s -t man | /usr/bin/man -l -

check:
	restview --long-description --strict

dist: man
	sudo python setup.py bdist_wheel

up:
	twine upload dist/`ls dist -rt | tail -1`


