#!/usr/bin/env python3

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    sys.exit()

packages = ['colout']

requires = ['argparse; python_version < "2.7"', 'pygments', 'babel']

setup_requires = ['setuptools_scm']

classifiers = """
Environment :: Console
License :: OSI Approved :: GNU General Public License v3 (GPLv3)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
""".strip().split('\n')

setup(
    name='colout',
    use_scm_version=True,
    classifiers=classifiers,
    description='Color Up Arbitrary Command Output.',
    long_description=open('README.md').read(),
    author='nojhan',
    author_email='nojhan@nojhan.net',
    url='http://nojhan.github.com/colout/',
    packages=packages,
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'colout': 'colout'},
    scripts=['bin/colout'],
    setup_requires=setup_requires,
    include_package_data=True,
    install_requires=requires,
    license='GPLv3',
    zip_safe=False,
)
