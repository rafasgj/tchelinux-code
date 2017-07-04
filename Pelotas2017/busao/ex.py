#!/usr/bin/env python

from collections import namedtuple
from random import random

def nextInt():
    return int(random()*200)

class Node(namedtuple('Node','key left right')):
    pass

def bst_insert(node, key):
    if node == None: return Node(key, None, None)
    if key <= node.key:
        return Node(node.key, bst_insert(node.left, key), node.right)
    else:
        return Node(node.key, node.left, bst_insert(node.right, key))

print(type(bst_insert))

