#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Numpy and general python utils

    Potentially can be sensibly split up at a later point
"""


############################
# Join dicts python2
############################
import numpy as np

dir(np)

import os
os.getcwd()


from __future__ import division
import collections
from collections import defaultdict


def join_two_dicts(a,
                   b,
                   a_val_name='a_val_name',
                   b_val_name='b_val_name',
                   create_inner_dict = True):

        """
            Useful when both dicts dont have same values
            Use create_inner_dict = True to identify value origins

            Method: Left Join
            Primary key in a: All values must be in a.
        """

        if create_inner_dict == True:
            # create inner dicts
            a = {key:{a_val_name:val} for key,val in a.items()}
            b = {key:{b_val_name:val} for key,val in b.items() if key in a }

        dd = defaultdict(list)
        for d in (a, b): # you can list as many input dicts as you want here
            for key, value in d.iteritems():
                dd[key].append(value)
        return dd



#update values of an old dict with another dict
dict1 = {'bookA': 1, 'bookB': 2, 'bookC': 3}
dict2 = {'bookC': 2, 'bookD': 4, 'bookE': 5}
dict2.update(dict1)
dict2

############################
# reload in Python3
############################
import importlib
importlib.reload(module)
