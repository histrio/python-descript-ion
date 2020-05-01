python-descript-ion
===================

[![Build Status](https://travis-ci.org/histrio/python-descript-ion.svg?branch=master)](https://travis-ci.org/histrio/python-descript-ion)
[![PyPI](https://img.shields.io/pypi/v/descript.svg)]()
[![Coverage Status](https://coveralls.io/repos/github/histrio/python-descript-ion/badge.svg)](https://coveralls.io/github/histrio/python-descript-ion)


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
