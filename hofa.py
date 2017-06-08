import sys
import operator

class Elem:
    def __init__(self,letter,value):
        self.letter=letter
        self.value=value
        self.left=None
        self.right=None
    def __repr__(self):
        return str((self.letter,self.value))


def getHistogram(text):
    hist={}
    for s in text:
        if s in hist:
            hist[s]+=1
        else:
            hist[s]=1
    return hist


def makeNodes(hist):
    nodes=[]
    for elem in hist:
        nodes.append((elem,hist[elem]))
    return nodesa


def makeLeafs(nodes):
    for i in range(len(nodes)):
        nodes[i]=Elem(nodes[i][0],nodes[i][1])
    return nodes


def makeTree(nodes):
    while len(nodes)>1:
        node=Elem(nodes[0].letter+nodes[1].letter,nodes[0].value+nodes[1].value)
        node.left=nodes[0]
        node.right=nodes[1]
        del nodes[0]
        del nodes[0]

        nodes.insert(0,node)
        i=0
        while i<len(nodes)-1 and nodes[i].value>nodes[i+1].value:
            temp=nodes[i]
            nodes[i]=nodes[i+1]
            nodes[i+1]=temp
            i+=1

def getCode(letter,node):
    if letter not in node.letter:
        return None
    if letter==node.letter:
        return ""
    elif letter in node.left.letter:
        return "1"+getCode(letter,node.left)
    else:
        return "0"+getCode(letter,node.right)





text="neka kuca stalno kuca na vratima pun mi kurac pa"
hist=getHistogram(text)
print(hist)
nodes=makeNodes(hist)
print(nodes)

#sort here
nodes=sorted(hist.items(),key=operator.itemgetter(1))
print(nodes)
nodes=makeLeafs(nodes)
print(nodes)
makeTree(nodes)
print(nodes)

code=""
for i in text:
    code+=getCode(i,nodes[0])
print(code)