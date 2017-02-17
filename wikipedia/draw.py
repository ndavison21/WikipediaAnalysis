import networkx as nx
import pylab as plt

g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
nx.draw(g)
plt.savefig('wikipedia.pdf')

