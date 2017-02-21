import sys
print "Importing Libraries."
sys.stdout.flush()
import networkx as nx
import matplotlib
import pickle

matplotlib.use('AGG')

import matplotlib.pyplot as plt

plt.ioff()

print "Reading in 100 Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_100.txt', create_using=nx.DiGraph(), nodetype=int)

print "Drawing Network (50)"
sys.stdout.flush()
spring_pos = nx.spring_layout(g, iterations = 50)
print "Saving Positions"
sys.stdout.flush()
with open('spring_pos_50.pickle', 'wb+') as handle:
    pickle.dump(spring_pos, handle, protocol=pickle.HIGHEST_PROTOCOL)

print "Drawing Network (100)"
sys.stdout.flush()
spring_pos = nx.spring_layout(g, iterations = 100)
print "Saving Positions"
sys.stdout.flush()
with open('spring_pos_100.pickle', 'wb+') as handle:
    pickle.dump(spring_pos, handle, protocol=pickle.HIGHEST_PROTOCOL)


# with open('filename.pickle', 'rb') as handle:
#     b = pickle.load(handle)
