from __future__ import print_function
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
import io
import codecs
import os
import sys

import iAnnotateSV

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst', 'CHANGES.rst')

setup(
    name='iCallSV',
    version=iAnnotateSV.__version__,
    description='The module helps to call structural variants using NGS data set on human.',
    long_description=long_description,
    include_package_data=True,
    url='https://github.com/rhshah/iCallSV',
    download_url='https://github.com/rhshah/iCallSV/tarball/0.0.1',
    author=iAnnotateSV.__author__,
    author_email='rons.shah@gmail.com',
    license=iAnnotateSV.__license__,
    platforms='any',
    packages=['iCallSV'],
    install_requires=[
        'pandas',
        'numpy',
    ],
    zip_safe=False,
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Development Status :: 3'
    ),
)