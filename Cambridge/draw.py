print "Importing Libraries."
import networkx as nx
import pylab as plt

print "Reading in Graph."
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)

print "Performing Spring Layout."
spring_pos = nx.spring_layout(g)

print "Drawing Network"
plt.axis("off")
nx.draw_networkx(g, pos = spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
plt.savefig('results/cam.pdf')
plt.close()
