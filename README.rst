*********************************************
Convert reStructuredText to Confluence markup
*********************************************

This is cloned from https://github.com/netresearch/rst2confluence.
See Changelog.

.. image:: https://travis-ci.org/netresearch/rst2confluence.svg?branch=master
    :target: https://travis-ci.org/netresearch/rst2confluence

====================
Supported directives
====================

- bullet list
- enumerated list
- image, figure, confluence image galleries
- definition list (with classifiers)
- simple and grid tables
- block quote
- text effect

  - strong
  - emphasis
  - monospace
- code blocks
- links
- admonitions

  - info
  - note
  - tip
  - warning
- field lists
- line blocks (except nested ones)
- meta directives
- substitutions


Additional features
===================

Excerpts
--------
When using the command line option ``--excerpt``, your
confluence code will mark up the first paragraph as excerpt__.

__ https://confluence.atlassian.com/doc/excerpt-macro-148062.html


Image galleries
---------------
Images and figures with class names that begin with
``gallery-`` form a gallery::

   .. image:: cat.jpg
       :class: gallery-1
   .. image:: dog.jpg
       :class: gallery-1
   .. figure:: horse.jpg
       :class: gallery-2
       :scale: 50%

This creates two galleries: One with cat and dog, the other one with
the horse picture only.
All attributes are ignored on gallery images.

Gallery-classed images are converted to ``{gallery:include=a.jpg,b.jpg}``
Confluence markup.

=====
Usage
=====
::

    ./rst2jira.py /path/to/file.rst


============
Installation
============
From git checkout::

    $ sudo ./setup.py install

Without a git checkout from the `Python Package Index`__::

    $ pip install rst2jira

__ https://pypi.python.org/pypi/rst2jira


============
Dependencies
============

- ``colordiff`` (for running the tests)

=====
Tests
=====
We have some examples how ``rst2jira`` should behave.

Check if it does what it should::

    ./run-tests.sh

Run a single test::

    ./run-test.sh test/figure.rst

