
print "Importing Libraries"

import sys
import networkx as nx
import community
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
plt.ioff

print "Reading in 100 Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_100.txt', create_using=nx.Graph(), nodetype=int)


# print "Convert to undirected."
# sys.stdout.flush()
# g_ud = g.to_undirected()

print "Claculating Best Partition."
sys.stdout.flush()
communities = community.best_partition(g)

values = [communities.get(node) for node in g.nodes()]

print "Drawing Network (Spring)"
sys.stdout.flush()
plt.figure(num=None, figsize=(100, 100))
plt.axis("off")
spring_pos = nx.spring_layout(g, iterations = 20)
nx.draw(g, pos=spring_pos, cmap=plt.get_cmap("jet"), node_color=values, with_labels = False, node_size = 100)
print "Saving Figure"
sys.stdout.flush()
plt.savefig('results/wiki_100_communites.pdf')
