import sys
print "Importing Libraries."
sys.stdout.flush()
import networkx as nx
import matplotlib

matplotlib.use('AGG')

import matplotlib.pyplot as plt

plt.ioff()

print "Reading in Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_1000.txt', create_using=nx.DiGraph(), nodetype=int)

print "Drawing Network (Spring)"
sys.stdout.flush()
plt.axis("off")
nx.draw_spring(g, with_labels = False, node_size = 35)
print "Saving Figure"
sys.stdout.flush()
plt.savefig('results/wiki_1000_spring.pdf')

print "Drawing Network (Spectral)"
sys.stdout.flush()
nx.draw_spectral(g, with_labels = False, node_size = 35)
print "Saving Figure"
sys.stdout.flush()
plt.savefig('results/wiki_1000_spectral.pdf')
plt.close()
