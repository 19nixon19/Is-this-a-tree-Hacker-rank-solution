#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'sExpression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING nodes as parameter.
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def sExpression(nodes):
    error = []
    aj = {}
    nodes = nodes.split(' ')
    for ele in nodes:
        start, end = ele[1], ele[3]
        if start not in aj:
            aj[start] = [end]
        else:
            for cur in aj[start]:
                if end == cur:
                    return 'E2'
            aj[start].append(end)
            if len(aj[start]) > 2:
                return 'E1'
            
    visited = set()
    head_set = {}
    for key, child in aj.items():
        child.sort()  
    for key, child in aj.items(): 
        if key not in visited:
            pass_by = set()
            node = TreeNode(key)
            if not dfs(key, visited, aj, pass_by, node, head_set, error):
                return error[0]
            head_set[key] = node

    if len(head_set) > 1:
        return 'E4'
    else:
        head = [ele for ele in head_set.values()][0]
        stack = []
        stack.append(head)
        return dfs_tree(head)
def dfs_tree(root):
    if not root:
        return ''
    else:
        left = dfs_tree(root.left)
        right = dfs_tree(root.right)
        return '(' + str(root.val) + left + right + ')'
 
 
def dfs(cur, visited, aj, pass_by, node, head_set, error):
    if node.val in pass_by: # E3
        error.append('E3')
        return False
    elif node.val in head_set:
        del head_set[node.val]
        return True
    pass_by.add(node.val)
    if node.val in aj:
 
        for child in aj[node.val]:
            if child in head_set:
                new = head_set[child]
            elif child in visited:
                error.append('E3')
                return False
            else:
                new = TreeNode(child)
            if not node.left:
                node.left = new
            elif not node.right:
                node.right = new
            else:
                error.append('E1')
                return False
            if not dfs(child, visited, aj, pass_by, new, head_set, error):
                return False
    visited.add(node.val)
    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nodes = input()

    result = sExpression(nodes)

    fptr.write(result + '\n')

    fptr.close()
