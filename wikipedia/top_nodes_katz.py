import networkx as nx
from sys import stdout

def get_top_keys(dictionary, top):
    items = dictionary.items()
    items.sort(reverse=True, key=lambda x: x[1])
    return items[:top]

print "Reading in Full Graph."
stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)

print "Katz."
stdout.flush()

katz = nx.katz_centrality_numpy(g)

file = open("results/katz.txt", "w+")
file.write("Top 100 Nodes by katz centrality\n")
for node in get_top_keys(katz, 100):
    file.write("{}, {}\n".format(node[0], node[1]))
file.close()

print "We Done Here."
