# 1.6 havel - hakimi
# check if a grades sequence is graphical

import networkx as nx
import matplotlib.pyplot as plt

def hh_custom( a ):
    """  Given a grades sequence check if it is graphical
        If it is return the list of edges and plot the graph. """

    # if not already sorted
    a.sort(reverse = True)

    # V is the sequence of nodes [ 1-n ]
    V = [i for i in range( 1,len(a)+1 )]

    # d is the list with each node and its grade
    D = []
    for a,v in zip(a,V):
        D.append([a,v])

    # E is the list with he edges
    E = []

    for i,d in enumerate(D):
        # print(D[i])
        # print(d[0],d[1],d[1][0])

        if d[0] > 0 :
            print ( "Working on node ",d[1]," with grade ",d[0])
            print ("Will create ",d[0]," new edges")
            grade = d[0]
            d[0] = 0
            maxnodes = []
            for c in D:
                maxnodes.append(c)
            maxnodes.sort(reverse = True)

            for y,node in enumerate(maxnodes):
                if node[0] >= 1 and grade >= 1 :
                    E.append([d[1],node[1]])
                    print ("New edge: ",[d[1],node[1]])
                    node[0] -= 1
                    # D[y][]
                    # maxnodes.sort(reverse = True)
                    print("List is now ",maxnodes)
                    grade -= 1
                else:
                    print("break! D = ",D)
                    break

        else:
            print("Finished in node ",d[1],"--->",D)
            break

    if max(D)[0] != 0:
        print("These nodes have been left unmatched")
        left = [d for d in D if d[0]>0]
        print(left)
        print ("Sequence is not graphical.")
        E = []
    else:
        G = nx.Graph()
        G.add_nodes_from(V)
        G.add_edges_from(E)
        nx.draw_networkx(G)
        plt.show()
        print ("New edges:")
        for e in E:
            print(e)
    return E



seq = [5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3]
seq2 = [6, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1]
hh_custom(seq2)
