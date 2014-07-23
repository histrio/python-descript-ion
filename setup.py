# -*- coding: utf-8 -*-
import sys
import os
from setuptools import setup

sys.path.insert(0, os.path.abspath("src"))

"""Simple library for descript.ion files manipulation"""

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="descript",
    version='0.0.1',
    description=__doc__,
    keywords="descript.ion file description handler",
    author="Rinat F Sabitov",
    author_email="rinat.sabitov@gmail.ru",
    maintainer='Rinat F Sabitov',
    maintainer_email='rinat.sabitov@gmail.com',
    url="https://github.com/histrio/python-descript-ion",
    package_dir={'': 'src'},
    packages=[".", ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Environment :: Web Environment',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    long_description=read('README'),
    test_suite='test',
    tests_require=['mock', 'nose'],
)
