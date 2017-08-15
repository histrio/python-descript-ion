python-descript-ion
===================

[![Build Status](https://travis-ci.org/histrio/python-descript-ion.svg?branch=master)](https://travis-ci.org/histrio/python-descript-ion)
[![PyPI](https://img.shields.io/pypi/v/descript.svg)]()

Simple library for `descript.ion` files manipulation 

Examples:
---------

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
