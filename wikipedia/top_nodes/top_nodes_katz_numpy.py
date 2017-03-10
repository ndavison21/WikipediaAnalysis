import networkx as nx
from sys import stdout

print "Reading in Full Graph."
stdout.flush()
g = nx.read_edgelist('../data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)

print "Katz."
stdout.flush()

with open("../results/rankings/katz_numpy.txt", "w+") as file:
    for n,k in nx.katz_centrality_numpy(g).items():
        file.write("{} {}\n".format(n, k))

print "We Done Here."
