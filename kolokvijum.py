"""
Resenje sadrzi algoritamske korake svih delova zadatka.
Oni nisu rasporedjeni u funkcije. Poslednji korak (decode) nije trazen ali je ovde zbog kompletnosti.
"""

## Tree element class

class Elem:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str((self.letter, self.value))

text = "This is a sample text. It is very short and dumb."

## Histogram

hist = {}
for s in text:
    if hist.has_key(s):
        hist[s] += 1
    else:
        hist[s] = 1
print "Hist: ", hist

## List of nodes from histogram, node is a tuple (letter, count)

nodes = []
for elem in hist:
    nodes.append((elem, hist[elem]))
print "Nodes: ", nodes
    
## Sort list using O(n^2) sort [bubble sort]

for i in range(len(nodes) - 1):
    for j in range(i+1, len(nodes)):
        if nodes[i][1] > nodes[j][1]:
            temp = nodes[i]
            nodes[i] = nodes[j]
            nodes[j] = temp
print "Sorted nodes: ", nodes

## Make leafs of the Huffman tree, replace tuples with objects

for i in range(len(nodes)):
    new_elem = Elem(nodes[i][0], nodes[i][1])
    nodes[i] = new_elem
print "Leafs: ", nodes

## Make Huffman tree

while len(nodes) > 1:
    # make new node by merging 1st and 2nd element of the list
    new_node = Elem(nodes[0].letter + nodes[1].letter, nodes[0].value + nodes[1].value)
    new_node.left = nodes[0]
    new_node.right = nodes[1]
    # replace first two nodes with the merged node
    del nodes[0]
    del nodes[0]
    nodes.insert(0, new_node)
    # insertion sort step to find the sorted location for the new node, to the right
    i = 0
    while i < len(nodes) - 1 and nodes[i].value > nodes[i+1].value:
        temp = nodes[i]
        nodes[i] = nodes[i+1]
        nodes[i+1] = temp
        i += 1
    print nodes   ## only the top node is printed, but others are saved in left and right subtrees

"""
Get code of letter (encode), recursive. Append 0 for the left subtree, 1 for the right subtree
"""
def getCode(letter, tree):
    node = tree
    if letter not in node.letter:
        return None
    if letter == node.letter:
        return ""
    elif letter in node.left.letter:
        return "0" + getCode(letter, node.left)
    else:
        return "1" + getCode(letter, node.right)

code = ""
for s in text:
    code += getCode(s, nodes[0])
print "Code: ", code
print "Original text length in bits: ", 8 * len(text)
print "Code length in bits: ", len(code)

"""
Get text corresponding to code (decode)
"""
def getText(code, tree):
    node = tree
    ans = ""
    for bit in code:
        if bit == "0":
            if node.left == None:
                ans += node.letter
                node = tree.left
            else:
                node = node.left
        else:
            if node.right == None:
                ans += node.letter
                node = tree.right
            else:
                node = node.right
    ans += node.letter
    return ans

new_text = getText(code, nodes[0])
print "Decoded text: ", new_text
