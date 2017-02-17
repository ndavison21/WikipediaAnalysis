print "Importing Libraries."
import networkx as nx
import pylab as plt

print "Reading in Graph."
g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)

print "Performing Spring Layout."
spring_pos = nx.spring_layout(g)

plt.axis("off")
print "Drawing Network"
nx.draw_networkx(g, pos = spring_pos, with_labels = False, node_size = 35)
plt.savefig('wikipedia.pdf')
plt.close()