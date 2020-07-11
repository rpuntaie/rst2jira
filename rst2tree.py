#!/usr/bin/env python

import sys
import codecs

txt = codecs.open(sys.argv[1], 'r', 'utf_8').read()

def rst2tree(txt):
    import docutils.parsers.rst
    parser = docutils.parsers.rst.Parser()
    document = docutils.utils.new_document("test")
    document.settings.tab_width = 4
    document.settings.pep_references = 1
    document.settings.rfc_references = 1
    parser.parse(txt, document)
    return document

doc = rst2tree(txt)

print(doc.pformat('  '))
