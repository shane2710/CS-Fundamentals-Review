#!/usr/bin/python

import sys
import os
import random

ds_path = os.path.abspath(os.path.join('../..'))
if ds_path not in sys.path:
    sys.path.append(os.path.join(ds_path, 'data-structures', 'tree'))

from tree import Tree

nums = [random.randint(0,10) for _ in range(0,10)]
bst = Tree(nums)

print(bst)
print(bst.dfs(10))
