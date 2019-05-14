import networkx as nx
import matplotlib.pyplot as plt

def readPaintingsFromFile(str):
    G = nx.Graph()

    try:
        f = open(str + ".txt","r")
    except:
        print("file not found")
        return G
    
    for x in f:
        splitString = x.rstrip('\n').split(" ")
        w = 0

        if(len(splitString) != 3):
            print("invalid string" + x)
            break

        if(splitString[0] not in G):
            G.add_node(splitString[0])
            
        if(splitString[2] not in G):
            G.add_node(splitString[2])

        if(splitString[1] == 'd'):
            w = 1
        elif(splitString[1] == 's'):
            w = 0
        else:
            print("invalid input")
            break
        G.add_edge(splitString[0],splitString[2],relation=splitString[1])

    return G

def printPaintingGraph(G):
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['relation'] == 'd']
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['relation'] == 's']

    pos = nx.planar_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color='b', style='dashed')

    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.show()

def examinePaintingGraph(G):

    nodes = G
    
    visited = set()
    X = set()
    Y = set()

    setSwitch = True
    
    def addToSet(b,c):
        if(b):
            X.add(c)
        else:
            Y.add(c)

    def checkConsistency(parent,child,b):

        if(G[parent][child]['relation'] == 's'):
            if(b):
                if(child not in X):
                    return False
            else:
                if(child not in Y):
                    return False
                    
        else:
            if(b):
                if(child in X):
                    return False
            else:
                if(child in Y):
                    return False
        return True

    def printFailure(parent,child):
        print("X = ", X)
        print("Y = ", Y)
        print(parent + " and " + child + " have relationship " 
        + G[parent][child]['relation'] + " which is impossible")

    for start in nodes:
        if start in visited:
            continue
        
        visited.add(start)
        addToSet(setSwitch,start)
        stack = [(start, iter(G[start]))]

        while stack:
            
            parent, children = stack[-1]

            try:
                child = next(children)

                if child not in visited:

                    visited.add(child)
                    
                    if(G[parent][child]['relation'] == 's'):
                        addToSet(setSwitch,child)

                    else:
                        setSwitch = not setSwitch
                        addToSet(setSwitch,child)

                    stack.append((child, iter(G[child])))

                else:
                    whichSet = False
                    if(parent in X):
                        whichSet = True
                    
                    if(not checkConsistency(parent,child,whichSet)):
                        printFailure(parent,child)
                        return False

            except StopIteration:
                stack.pop()
            
    print("Painter 1 created = ", X)
    print("Painter 2 created = ", Y)
    return True


Graph2 = readPaintingsFromFile("paintingtest")
examinePaintingGraph(Graph2)
printPaintingGraph(Graph2)
