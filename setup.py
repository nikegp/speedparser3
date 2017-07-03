#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for speedparser."""

from setuptools import setup, find_packages

try:
    from speedparser3 import VERSION
    version = ".".join(map(str, VERSION))
except:
    version = '0.3.1'

# some trove classifiers:

# License :: OSI Approved :: MIT License
# Intended Audience :: Developers
# Operating System :: POSIX

setup(
    name='speedparser3',
    version=version,
    description="Python3 version of speedparser https://github.com/jmoiron/speedparser",
    long_description=open('README.rst').read(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Development Status :: 4 - Beta',
    ],
    keywords='feedparser speedparser rss atom rdf lxml python3',
    author='Nike Gurin-Petrovych',
    author_email='nike.gurin@gmail.com',

    url='https://github.com/nikegp/speedparser3',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    install_requires=[
      # -*- Extra requirements: -*-
      'lxml',
      'chardet',
    ],
    python_requires='>=3.5',
    entry_points="""
    # -*- Entry points: -*-
    """,
)
