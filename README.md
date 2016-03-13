python-descript-ion
===================

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





Tests:
-----

[![Build Status](https://drone.io/github.com/histrio/python-descript-ion/status.png)](https://drone.io/github.com/histrio/python-descript-ion/latest)
