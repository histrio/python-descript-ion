# python-descript-ion

[![Build Status](https://travis-ci.org/histrio/python-descript-ion.svg?branch=master)](https://travis-ci.org/histrio/python-descript-ion)
[![PyPI](https://img.shields.io/pypi/v/descript.svg)]()
[![Documentation Status](https://readthedocs.org/projects/python-descript-ion/badge/?version=latest)](https://python-descript-ion.readthedocs.io/en/latest/?badge=latest)

Simple library for `descript.ion` files manipulation 

## Examples:

    import descript.ion

    #Read description
    with descript.ion.open(filename) as f:
        print f.description

    #Write description
    with descript.ion.open(filename) as f:
        f.description = self.description

    #Remove description
    with descript.ion.open(filename) as f:
        del f.description
