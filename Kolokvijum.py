import sys

text = "This is a sample text. It is very short and dumb."

class Elem:
    def __init__(self,letter,value):
        self.l = None
        self.r = None
        self.letter = letter
        self.value = value

    def __repr__(self):
        return str((self.letter,self.value))

def makeHist(text):
    hist = {}
    for s in text:
        if s in hist:
            hist[s] += 1
        else:
            hist[s] = 1
    return hist

def makeList(hist):
    nodes = []
    for i in hist:
        nodes.append((i,hist[i]))
    return nodes

def sorted(nodes):
    for i in range(len(nodes)-1):
        for j in range(i + 1, len(nodes)):
            if(nodes[i][1] > nodes[j][1]):
                temp = nodes[i]
                nodes[i] = nodes[j]
                nodes[j] = temp
    return nodes

def makeLeafs(nodes):
    for i in range(len(nodes)):
        nodes[i] = Elem(nodes[i][0],nodes[i][1])
    return nodes

def Tree(nodes):
    while len(nodes) > 1:
        new_node = Elem(nodes[0].letter + nodes[1].letter, nodes[0].value + nodes[1].value)
        new_node.l = nodes[0]
        new_node.r = nodes[1]
        del nodes[0]
        del nodes[0]
        nodes.insert(0, new_node)
        i = 0
        while i < len(nodes) - 1 and nodes[i].value > nodes[i+1].value:
            temp = nodes[i]
            nodes[i] = nodes[i+1]
            nodes[i+1] = temp
            i += 1
        print nodes
        print

def getCode(letter,tree):
    node = tree
    if letter not in node.letter:
        return None
    if letter == node.letter:
        return ""
    elif letter in node.l.letter:
        return "0"+getCode(letter,node.l)
    else:
        return "1"+getCode(letter,node.r)

def getText(code,tree):
    node = tree
    ans = ""
    for bit in code:
        if bit == "0":
            if node.l == None:
                ans += node.letter
                node = tree.l
            else:
                node = node.l
        else:
            if node.r == None:
                ans += node.letter
                node = tree.r
            else:
                node = node.r
    ans += node.letter
    return ans

hist = makeHist(text)
print hist
print

nodes = makeList(hist)
print nodes
print

nodes = sorted(nodes)
print nodes
print

nodes = makeLeafs(nodes)
print nodes
print

Tree(nodes)

code = ""
for s in text:
    code += getCode(s, nodes[0])
print "Code: ", code
print "Original text length in bits: ", 8 * len(text)
print "Code length in bits: ", len(code)

new_text = getText(code, nodes[0])
print (new_text)