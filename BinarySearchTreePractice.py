import sys
import random
import string
import operator

global x

# Random list of integers

def random_list(min, max, elements):
    return random.sample(range(min,max),elements)

# Random strings

def random_strings(size = 5, chars = string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in  range(size))

# Making list of strings

def add_list(B,element,size):
    B.insert(0,element)
    return B[:size]

# Node

class Node:

    # Constructor

    def __init__(self, key, data):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key  # key
        self.data = data   # data

    def __repr__(self):
        return str((self.data,self.key))

# Tree

class Tree:
    
    # Constructor
    
    def __init__(self):
        self.root = None

    # Add node to tree

    def tree_insert(self,key,data):
        node = Node(key,data)
        if self.root == None:
            self.root = node
        else:
            self._tree_insert(self.root,node)
    
    def _tree_insert(self,treeNode,newNode):
        if(treeNode.key >= newNode.key):
            if treeNode.left == None:
                treeNode.left = newNode
                newNode.parent = treeNode
            else:
                return self._tree_insert(treeNode.left,newNode)
        else:
            if treeNode.right == None:
                treeNode.right = newNode
                newNode.parent = treeNode
            else:
                return self._tree_insert(treeNode.right,newNode)
        
    # Print tree inorder
    
    def inorder_walk(self,node):
        global x
        if node != None:
            self.inorder_walk(node.left)
            print("Node : ", node.key, node.data)
            self.inorder_walk(node.right)

    # Root print

    def tree_root_print(self) :
        if(self.root != None) :
            print("Printing root data", self.root.key, self.root.data)

    # Search tree
    
    def tree_search(self, node, key):
        if node == None or node.key == key:
            return node
        if key < node.key:
            return self.tree_search(node.left,key)
        else:
            return self.tree_search(node.right,key)

    # Itterative tree search

    def itterative_tree_search(self, node, key):
        while node != None and node.key != key:
            if node.key > key:
                node = node.left
            else:
                node = node.right
        return node

    # Maximum
    
    def tree_max(self,node):
        while node.right != None:
            node = node.right
        return node

    # Minimum

    def tree_min(self, node):
        while node.left != None:
            node = node.left
        return node

    # Successor

    def tree_successor(self,node):
        if(node != None):
            if node.right != None:
                return self.tree_min(node.right)
            while node.parent != None and node.parent.right == node:
                node = node.parent
            return node.parent
        else:
            return None
        

    # Ancestor

    def tree_ancestor(self,node):
        if node != None or node != self.tree_min(node):
            if node.left != None:
                return self.tree_max(node.left)
            while node.parent != None and node.parent.left == node:
                node = node.parent
            return node.parent
        else:
            return None

     # Delete

    def tree_delete(self,node):
        if node.left is None:
            tree.transplant(node, node.right)
        elif node.right is None:
            tree.transplant(node, node.left)
        else:
            y = tree.tree_min(node.right)
            if y.parent != node:
                tree.transplant(y,y.right)
                y.right = node.right
                y.right.parent = y
            tree.transplant(node,y)
            y.left = node.left
            y.left.parent = y 
            

    def transplant(self,node,node2):
        if node == None:
            self.root = node2
        elif node.parent.left == node:
            node.parent.left = node2
        else:
            node.parent.right = node2
        if node2 != None:
            node2.parent = node.parent

    # Append

    def tree_append(self,node):
        global x
        if node != None:
            self.tree_append(node.left)
            x.append(node)
            self.tree_append(node.right)

    # Depth

    def tree_depth(self, node):
        if node is not None:
            ldepth = self.tree_depth(node.left)
            rdepth = self.tree_depth(node.right)
        else:
            return 0
        return max(ldepth,rdepth) + 1

    # Size
    
    def tree_size(self,node):
        if node is None:
            return 0
        else:
            return self.tree_size(node.left) + 1 + self.tree_size(node.right)

tree = Tree()            

text="napusi se kurca kastelaneeee"

hist={}

for s in text:
    if s in hist:
        hist[s]+=1
    else:
        hist[s]=1

print hist
print

nodes = []

for i in hist:
    nodes.append((i,hist[i]))
print nodes
print

nodes = sorted(hist.items(), key = operator.itemgetter(1))
print nodes
print

for i in range(len(nodes)):
    tree.tree_insert(nodes[i][1], nodes[i][0])

tree.inorder_walk(tree.root)

current = tree.itterative_tree_search(tree.root, nodes[3][1])
print(current.key,current.data,tree.tree_successor(current).key,tree.tree_successor(current).data)
print(current.key,current.data,tree.tree_ancestor(current).key,tree.tree_ancestor(current).data)
print


"""
A = random_list(0,50,20)

B = [None] * 20

for i in range(0,len(B)):
    B = add_list(B,random_strings(),20)

for i in range(0,len(A)):
    tree.tree_insert(A[i], B[i])

print(A)
print
print(B)
print
tree.tree_root_print()
print
tree.inorder_walk(tree.root)
print

if tree.tree_search(tree.root, A[5]):
    print("Node with key: ", A[5],"and data: ", B[5], "found")
else:
    print("Node with not found")
print

if tree.itterative_tree_search(tree.root, A[2]):
    print("Node with key: ", A[2],"and data: ", B[2], "found")
else:
    print("Node with not found")
print

print(tree.tree_max(tree.root).key, tree.tree_max(tree.root).data)
print
print(tree.tree_min(tree.root).key, tree.tree_min(tree.root).data)
print

current = tree.itterative_tree_search(tree.root, A[7])
print(current.key,current.data,tree.tree_successor(current).key,tree.tree_successor(current).data)
print

current = tree.itterative_tree_search(tree.root, A[7])
print(current.key,current.data,tree.tree_ancestor(current).key,tree.tree_ancestor(current).data)
print

x = list()
tree.tree_append(tree.root)

for i in x:
    print(i.key,i.data)
print

node_delete = tree.tree_search(tree.root,A[5])
tree.tree_delete(node_delete)

tree.inorder_walk(tree.root)
print

print(tree.tree_depth(tree.root))
print(tree.tree_size(tree.root))


"""


