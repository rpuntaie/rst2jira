#!/usr/bin/env python

from setuptools import setup
import os
from os.path import dirname

here = os.path.abspath(dirname(__file__))
os.chdir(here)

with open(os.path.join(here, 'README.rst'), 'rt') as f:
    long_description = f.read()

setup(
    name='rst2jira',
    version='0.7.2',
    description='reStructuredText to confluence/jira markup converter',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Kenichiro TANAKA',
    author_email='tanaka.kenichiro@gmail.com',
    maintainer='Roland Puntaier',
    maintainer_email='roland.puntaier@gmail.com',
    url='https://github.com/rpuntaie/rst2jira',
    license='AGPL',
    data_files=[("man/man1", ["rst2jira.1"])],
    python_requires='>=3.6',
    classifiers=[
                    'Development Status :: 4 - Beta',
                    'Environment :: Console',
                    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python :: 3',
                    'Intended Audience :: End Users/Desktop',
                    'Intended Audience :: Information Technology',
                    'Topic :: Utilities'],
    install_requires=['docutils', 'Pygments'],
    py_modules=['rst2confluence.confluence'],
    scripts=['scripts/rst2jira.py']
)
