#!/usr/bin/python

import sys
import os

ds_path = os.path.abspath(os.path.join('..'))
if ds_path not in sys.path:
    sys.path.append(os.path.join(ds_path, 'data_structures', 'tree'))

from bst import BST
