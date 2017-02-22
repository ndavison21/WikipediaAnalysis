import sys
import networkx as nx
import random as rand
from numpy import random

g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)

target_nodes = 0.15 * nx.number_of_nodes(g)

print "Target Nodes:", target_nodes

print nx.info(g)

g_sample = nx.DiGraph()
p = 0.15
steps = 0
limit = 500

finished = False
while not(finished):
    print "Sample has", nx.number_of_nodes(g_sample), "nodes. Target:", target_nodes
    source = rand.choice(g.nodes())
    node = source
    steps = 0
    while(steps < limit):
        steps = steps + 1
        if rand.random() < p:
            node = source
        nodes = g.neighbors(node)
        if (len(nodes) == 0):
            continue
        next_node = rand.choice(nodes)
        if not(g_sample.has_edge(node, next_node)):
            g_sample.add_edge(node, next_node)
            steps = 0
            node = next_node
            if nx.number_of_nodes(g_sample) >= target_nodes:
                finished = True
                break



print nx.info(g_sample)

outfile = open("cambridge_net_rw.txt", "wb+")
nx.write_edgelist(g_sample, outfile)