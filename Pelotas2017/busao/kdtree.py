from collections import namedtuple
from operator import itemgetter
from pprint import pformat

import math

def manhathan(v1,v2):
    dist = 0 
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])
    return dist

def euclidean(v1,v2):
    sqsum = 0 
    for i in range(len(v1)):
        v = v1[i] - v2[i]
        sqsum += v * v
    return math.sqrt(sqsum)

class Node(namedtuple('Node', 'location left right')):
    def __repr__(self):
        return pformat(tuple(self))

class KDTree:

    def __init__(self, point_list):
        self.root = KDTree.__create_node(point_list)

    def __repr__(self):
        return self.root.__repr__()

    @staticmethod
    def __create_node(point_list, depth=0):
        try:
            k = len(point_list[0]) # assumes all points have the same dimension
        except IndexError as e: # if not point_list:
            return None
        # Select axis based on depth so that axis cycles through all valid values
        axis = depth % k
        # Sort point list and choose median as pivot element
        point_list.sort(key=itemgetter(axis))
        median = len(point_list) // 2 # choose median
        v = point_list[median][axis]
        while median+1 < len(point_list) and point_list[median+1][axis]==v:
            median += 1
    
        # Create node and construct subtrees
        return Node(
            location=point_list[median],
            left=KDTree.__create_node(point_list[:median], depth + 1),
            right=KDTree.__create_node(point_list[median + 1:], depth + 1)
        )

    @staticmethod
    def kdtree_find(node, reference, depth=0):
        if node == None or node.location == reference:
            return node
        axis = depth % len(node.location)
        if reference[axis] <= node.location[axis]:
            return kdtree_find(node.left, reference, depth + 1)
        return kdtree_find(node.right, reference, depth + 1)

    @staticmethod
    def __add_to_nn(c, cnt, l):
        last = c[-1]
        if len(c) == cnt and last[1] < l[1]: return c
        c.append(l)
        c.sort(key=itemgetter(1))
        return c[:cnt]

    @staticmethod
    def __nn(n, r, c, depth=0,dist=euclidean,cnt=1):
        axis = depth % len(n.location)
        v = r[axis]
        if not (n.left == None and n.right == None):
            left_first = True
            if v < n.location[axis] and n.left != None:
                c = KDTree.__nn(n.left, r, c, depth+1, dist, cnt)
            elif n.right != None:
                c=KDTree.__nn(n.right, r, c, depth+1, dist, cnt)
                left_first = False
        else:
            d = dist(n.location,r)
            return KDTree.__add_to_nn(c,cnt,(n[0],d))

        s = list(r[:])
        s[axis] = n.location[axis]
        hd = dist(s,r)
        _,cd = c[-1]
        if hd <= cd or len(c) < cnt:
            if left_first and n.right != None:
                c = KDTree.__nn(n.right,r,c,depth+1,dist,cnt)
            elif not left_first and n.left != None:
                c = KDTree.__nn(n.left,r,c,depth+1,dist,cnt)
        
        d = dist(n.location,r)
        return KDTree.__add_to_nn(c,cnt,(n[0],d))

    def getClosestPoint(self, reference, distance=euclidean):
        result,*_ = KDTree.__nn(self.root, reference, [(None,float("inf"))], dist=distance)
        return result

    def getClosestPoints(self, reference, count, distance=euclidean):
        return KDTree.__nn(self.root, reference, [(None,float("inf"))], dist=distance, cnt=count)

def main():
    """Example usage"""
    point_list = [(5,8),(2,3),(5,4),(9,6),(4,7),(5,3),(5,9),(8,1),(7,2)]
    tree = KDTree(point_list)
    print(tree)
    print("---------------------------------------------")
    print("Searching (1,0)...")
    print(tree.getClosestPoint((1,0)))
    print("---------------------------------------------")
    print("Searching (4,6)...")
    print(tree.getClosestPoint((4,6)))
    print("---------------------------------------------")
    print("Searching (10,5)...")
    print(tree.getClosestPoint((10,5)))
    print("---------------------------------------------")
    print("Searching (6,8)...")
    print(tree.getClosestPoint((6,8)))
    print("---------------------------------------------")
    print("Searching (6,8) with Manhattan distance...")
    print(tree.getClosestPoint((6,8),distance=manhathan))
    print("---------------------------------------------")
    print("Searching 3 points close to (4,8)...")
    print(tree.getClosestPoints((4,8),count=3))
    print("---------------------------------------------")

if __name__ == '__main__':
    main()
