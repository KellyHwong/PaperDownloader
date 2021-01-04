#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import sys
import codecs
from setuptools import setup, find_packages
from cvf_downloader import __version__, __author__, __email__

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]


def long_description():
    with codecs.open('README.rst', 'rb') as readme:
        if not sys.version_info < (3, 0, 0):
            return readme.read().decode('utf-8')


setup(
    name='cvf_downloader',
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="paper downloading helper for CVF conference papers",
    # long_description=long_description(),
    keywords=['cvf', 'papers'],
    maintainer=__author__,
    maintainer_email=__email__,
    license="GPLv3",
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/KellyHwong/cvf_downloader',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GPLv3 License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'cvf_downloader = cvf_downloader.main:main',
        ]
    },
)
