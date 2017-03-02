import sys
import networkx as nx
import random as rand
from numpy import random

print "Reading Graph"
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)

target_nodes = 0.15 * nx.number_of_nodes(g)

print "Target Nodes:", target_nodes
sys.stdout.flush()

print "Attempting with limit of 100,000"
sys.stdout.flush()

g_sample = nx.DiGraph()
p = 0.15
steps = 0
limit = 100000

finished = False
while not(finished):
    print "Sample has", nx.number_of_nodes(g_sample), "nodes. Target:", target_nodes
    sys.stdout.flush()
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

outfile = open("data/wiki-Talk_rw_100000.txt", "wb+")
nx.write_edgelist(g_sample, outfile)
outfile.close()

print "\nAttempting with limit of len(g)"
sys.stdout.flush()

g_sample = nx.DiGraph()
limit = 100 * nx.number_of_nodes(g)

finished = False
while not(finished):
    print "Sample has", nx.number_of_nodes(g_sample), "nodes. Target:", target_nodes
    sys.stdout.flush()
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

outfile = open("data/wiki-Talk_rw_leng.txt", "wb+")
nx.write_edgelist(g_sample, outfile)
outfile.close()

