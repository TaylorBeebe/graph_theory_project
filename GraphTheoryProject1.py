import networkx as nx
import matplotlib.pyplot as plt

def readTimelineFromFile(str):

    G = nx.DiGraph()
    try:
        f = open(str + ".txt","r")
    except:
        print("file not found")
        return G


    for x in f:
        splitString = x.rstrip('\n').split(" ")
        
        if(len(splitString) < 3):
            print("invalid string" + x)
            break

        if(splitString[0] + ' birth' not in G):
            G.add_node(splitString[0] + ' birth',bipartite=0)
            G.add_node(splitString[0] + ' death',bipartite=1)
            G.add_edge(splitString[0] + ' birth', splitString[0] + ' death')
        
        if(splitString[2] + ' birth' not in G):
            G.add_node(splitString[2] + ' birth',bipartite=0)
            G.add_node(splitString[2] + ' death',bipartite=1)
            G.add_edge(splitString[2] + ' birth', splitString[2] + ' death')
        
        if(splitString[1] == 'b'):
            G.add_edge(splitString[0] + ' death', splitString[2] + ' birth')

        elif (splitString[1] =='s'):
            G.add_edge(splitString[0] + ' birth', splitString[2] + ' death')
            G.add_edge(splitString[2] + ' birth', splitString[0] + ' death')
        
        else:
            print("invalid string" + x)
            break

    return G

def topSortDAG(G):

    try:
        print(list(nx.topological_sort(G)))
        top = nx.bipartite.sets(G)[0]
        pos = nx.bipartite_layout(G, top)
        nx.draw(G,pos, with_labels=True, font_weight='bold')
        plt.show()
    except:
        print("Input data is inconsistent")


#Tests
Graph = readTimelineFromFile("birthdeathtest")
topSortDAG(Graph)
