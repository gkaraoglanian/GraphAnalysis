#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: gk
Grigoris Karaoglanian

"""

import networkx as nx
import matplotlib.pyplot as plt

def t_sorting(G):
    """ 
        Topological sorting of a directed graph.
    """
    if nx.is_directed(G):
        # show initial graph
        nx.draw(G,with_labels = True)
        plt.show()
        L = []  # a list to put the topological sorting
        while G.order() != 0 :
            circuitcheck = [] # a list for each node that has
            # in_degree == out_degree
            # if number of nodes == len (circuitcheck) then 
            # graph is a circuit and t_sorting is not possible.
            for node in G:
                if G.order() > 1 and G.in_degree(node) == G.out_degree(node):
                    circuitcheck.append(node)
            if len(circuitcheck) < G.order():
                rmnodes = [] # nodes to remove after iteration
                rmedges = [] # edges to remove after iteration
                # for every node in G that has in_degree == 0
                # the node is removed and goes into L
                for node in G:
                    if G.in_degree(node) == 0 :
                        L.append(node)
                        rmnodes.append(node)
                        # for each node that is about to be removed
                        # its edges shall be removed also
                        for succ in G.successors(node):
                            rmedges.append([node,succ])
                # Iteration is over, dictionaries can change
                # Nodes and edges can now be removed
                G.remove_edges_from(rmedges)
                G.remove_nodes_from(rmnodes)
                print ("Removed nodes: ",rmnodes)
                print ("Removed Edges: ",rmedges)
                print("G is now: ",G)
                print("Nodes: ",G.nodes())
                # print("In_Degree: ",G.in_degree(G))
                # print("Out_Degree: ",G.out_degree(G))
                print("Edges :",G.edges())
            else:
                print ("Graph has a circuit. Topological sorting is not possible.")
                break
            
            nx.draw(G,with_labels = True)
            plt.show()
        else:
            # if G.order() == 0 :
            print ("A topological sorting is: ",L)
            
    else:
        try:
            Gdir = nx.to_directed(G)
            t_sorting(Gdir)
        except nx.NetworkXError:
            print("Requested Graph is not directed. Please insert a directed Graph.")
       
            
# ------- Several use case scenarios ----------
# Uncomment the ones you want to try           

## Returns the growing network (GN) digraph with n nodes.
# G = nx.gn_graph(6)

## In case of a non directed graph
# G = nx.complete_graph(2)

# Directed Graph with a circuit
G = nx.DiGraph()
G.add_nodes_from(range(1,5))
G.add_edges_from([(1,2),(2,5),(5,4),(4,1),(3,1),(3,2),(3,4)])

# Exercise 1.30 - 1h_seira
G = nx.DiGraph()
G.add_nodes_from(range(1,9))
G.add_edges_from([(1,8),(2,9),(2,6),(3,8),(4,1),(4,9),(6,1),(6,8),(7,5),(8,5),(8,7),(9,8)])
t_sorting(G)

# ----------------------------------------------------------------
# answer : A topological sorting is:  [2, 3, 4, 6, 9, 1, 8, 7, 5] |
# ----------------------------------------------------------------