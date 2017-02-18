print "Importing Libraries"

import networkx as nx
import community
import matplotlib.pyplot as plt

print "Reading in Graph."
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."

print "Need to convert to undirected graph."
g_ud = g.to_undirected()

print "Performing Spring Layout."
spring_pos = nx.spring_layout(g_ud)

print "Claculating Best Partition."
communities = community.best_partition(g_ud)
print "Partitioning Done!"

values = [communities.get(node) for node in g_ud.nodes()]

print "Generating Output"
plt.axis("off")
nx.draw_networkx(g, cmap=plt.get_cmap("jet"), node_color=values, node_size=35, with_labels=False)
plt.savefig("results/communities.pdf")
plt.close()