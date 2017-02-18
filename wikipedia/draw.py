print "Importing Libraries."
import networkx as nx
import matplotlib

matplotlib.use('AGG')

import matplotlib.pyplot as plt

plt.ioff()

print "Reading in Graph."
g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)

print "Performing Spring Layout."
spring_pos = nx.spring_layout(g)

print "Drawing Network"
plt.axis("off")
nx.draw_networkx(g, pos = spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
plt.savefig('results/wiki.pdf')
plt.close()
