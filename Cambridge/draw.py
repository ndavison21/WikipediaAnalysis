print "Importing Libraries."
import networkx as nx
import matplotlib
from networkx.drawing.nx_agraph import graphviz_layout

matplotlib.use('AGG')

import matplotlib.pyplot as plt

plt.ioff()

print "Reading in Graph."
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)

print "Drawing Network (Spring)"
plt.axis("off")
nx.draw_spring(g, with_labels = False, node_size = 35)
print "Saving Figure"
plt.savefig('results/cam_spring.pdf')

print "Drawing Network (Spectral)"
nx.draw_spectral(g, with_labels = False, node_size = 35)
print "Saving Figure"
plt.savefig('results/cam_spectral.pdf')
plt.close()
