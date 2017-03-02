import sys
import networkx as nx
import random as rand
from numpy import random

print "Reading Graph"
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)

target_nodes = 0.15 * nx.number_of_nodes(g)

print "Target Nodes:", target_nodes
sys.stdout.flush()

print "Attempting with limit of len(g)"
sys.stdout.flush()

g_sample = nx.Graph()
p = 0.15
steps = 0
limit = nx.number_of_nodes(g)

finished = False
while not(finished):
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
    if (steps >= limit):
        print "Steps Limit Reached. Sample has", nx.number_of_nodes(g_sample), "nodes. Target:", target_nodes
        sys.stdout.flush()

g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
file = open("data/wiki-Talk_rw_leng.txt", "w+")
for u, v in g_sample.edges_iter():
    if g.has_edge(u, v):
        file.write("{} {}\n".format(u, v))
    if g.has_edge(v, u):
        file.write("{} {}\n".format(v, u))
file.close()


print "Getting Giant Component"
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_rw_leng.txt', create_using=nx.DiGraph(), nodetype=int)
g_ud = g.to_undirected()

print "Getting connected subgraphs."
sys.stdout.flush()
connected_subgraphs = nx.connected_component_subgraphs(g_ud)
print "Getting connected giant component."
sys.stdout.flush()
sg = max(connected_subgraphs, key=len)
print "Got connected giant component"

file = open("data/sample_leng_giant_component.txt", "w+")
for u, v in sg.edges_iter():
    if g.has_edge(u, v):
        file.write("{} {}\n".format(u, v))
    if g.has_edge(v, u):
        file.write("{} {}\n".format(v, u))
file.close()


file = open("results/sample/leng_basic_info.txt", "w+")

file.write("*** Sample Graph ***\n")
print "Basic Graph Info."
sys.stdout.flush()
file.write(nx.info(g))

print "Reciprocity."
sys.stdout.flush()
reciprocated = 0
for (u,v) in g.edges_iter():
    if g.has_edge(v, u):
        reciprocated = reciprocated + 1
file.write("\nReciprocity: {}\n".format(float(reciprocated)/nx.number_of_edges(g)))
file.flush()
print "Clustering."
sys.stdout.flush()
file.write("Clustering: {}\n".format(nx.average_clustering(g.to_undirected())))

file.close()