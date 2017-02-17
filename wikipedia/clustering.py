print "Importing Libraries"

import networkx as nx
import pylab as plt
import numpy as np
from scipy import optimize

print "Reading in Graph."
g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported, analysing and plotting node clustering coefficients."

clusterings = nx.clustering(g)
values = sorted(sorted(set(in_degrees.values())))
hist = [clusterings.values().count(x) for x in values]

print "Drawing Clusterings (linear scale)"
plt.figure()
plt.grid(True)
plt.loglog(values, hist, 'ro-')
plt.legend(['Clustering Coefficient'])
plt.xlabel('Clustering Coefficient')
plt.ylabel('Number of Nodes')
plt.title('Wikipedia Talk Network')
plt.xlim([0, max(values)])
plt.savefig('results/clustering_coefficient.pdf')
plt.close()

print "Drawing Clusterings (log scale)"
plt.figure()
plt.grid(True)
plt.loglog(values, hist, 'ro-')
plt.legend(['Clustering Coefficient'])
plt.xlabel('Clustering Coefficient')
plt.ylabel('Number of Nodes')
plt.title('Wikipedia Talk Network')
plt.xlim([0, max(values)])
plt.savefig('results/log_clustering_coefficient.pdf')
plt.close()

print "We Done Here."
