import sys
print "Importing Libraries."
sys.stdout.flush()
import networkx as nx
import matplotlib
import pickle

matplotlib.use('AGG')

import matplotlib.pyplot as plt

plt.ioff()

print "Reading in Graph"
sys.stdout.flush()
g = nx.read_edgelist('wiki-Talk_100.txt', create_using=nx.DiGraph(), nodetype=int)

print "Reading in Positions (50)"
sys.stdout.flush()
with open('spring_pos_50.pickle', 'rb') as handle:
    spring_pos = pickle.load(handle)

print "Drawing Network (50)"
sys.stdout.flush()
plt.axis("off")
nx.draw(g, spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
plt.savefig('results/wiki_50.pdf')

print "Reading in Positions (100)"
sys.stdout.flush()
with open('spring_pos_100.pickle', 'rb') as handle:
    spring_pos = pickle.load(handle)

print "Drawing Network (Spring)"
sys.stdout.flush()
plt.axis("off")
nx.draw(g, spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
plt.savefig('results/wiki_100.pdf')
