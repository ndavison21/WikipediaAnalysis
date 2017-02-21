print "Importing Libraries."
import networkx as nx
import matplotlib
import pickle

matplotlib.use('AGG')

import matplotlib.pyplot as plt

plt.ioff()

print "Reading in Graph"
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)


with open('spring_pos_100.pickle', 'rb') as handle:
    spring_pos = pickle.load(handle)

print "Drawing Network (Spring)"
plt.axis("off")
nx.draw(g, spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
plt.savefig('results/cam_spring.pdf')
