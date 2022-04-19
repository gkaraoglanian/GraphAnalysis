#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 1.22
Find a eulerian circuit in a k-complete graph.

@author: gk
"""
import networkx as nx
import matplotlib.pyplot as plt

def Eulerian_c(n):
    """
    Parameters
    ----------
    n : int
    
    Plots the Kn complete graph and its eulerian circuit (if exists)

    Returns
    -------
    edgelabels : dict of ordered edges with their labels

    """
    # if n % 2 != 0:   could also be a valid condition
    try:
        G = nx.complete_graph(n)
        # create labels to show the path of the eulerian circuit
        edgelabels = {}
        for i,edge in enumerate(list(nx.eulerian_circuit(G))):
            edgelabels[edge] = i 
        print("A eulerian circuit is: ",edgelabels)
        # draw the complete graph
        nx.draw_networkx(G,pos=nx.circular_layout(G),with_labels = True, width = 3.0 , edge_color = 'black')
        # draw the eulerian circuits edges
        nx.draw_networkx_edges(G, pos=nx.circular_layout(G),edgelist=list(nx.eulerian_circuit(G)),width = 0.5 , edge_color = 'yellow' , arrows= True, arrowsize = 15)
        # put labels in circuits edges
        nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G),edge_labels=edgelabels,font_size = 7 , font_color = 'black' , rotate = False)
        plt.show()
        return edgelabels
    except nx.NetworkXError:
        print("K",n," is not Eulerian")
        
try:
    print("Insert an integer n to see if the n-complete graph is Eulerian and find a circuit")
    n = int(input("Enter n: "))
    Eulerian_c(n)
except ValueError:
    print("Sorry you can only insert an integer")