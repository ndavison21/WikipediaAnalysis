import networkx as nx
from sys import stdout

print "Reading in Full Graph."
stdout.flush()
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)

print "Katz."
stdout.flush()

with open("results/katz_numpy.txt", "w+") as file:
    for n,k in nx.eigenvector_centrality_numpy(g).items():
        file.write("{} {}\n".format(n, k))

print "We Done Here."
