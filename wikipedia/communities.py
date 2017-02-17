print "Importing Libraries"

import networkx as nx
import community
import matplotlib.pyplot as plt

print "Reading in Graph."
g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)
print "Graph Imported, detecting communities."

communities = community.best_partition(g)
print "Community detection done!"

values = [parts.get(node) for node in G_fb.nodes()]

print "Generating Output"
plt.axis("off")
nx.draw_networkx(g, cmap=plt.get_cmap("jet"), node_color=values, node_size=35, with_labels=False)
plt.savefig("results/communities.png", format = "PNG")
