
print "Importing Libraries"

from sys import stdout
import networkx as nx
import community
import json

print "Reading in Graph."
stdout.flush()
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.Graph(), nodetype=int)


print "Claculating Best Partition."
stdout.flush()
communities = community.best_partition(g)


with open("results/communities.txt", "w+") as f:
    json.dump(communities, f)

# load from file:
# with open("results/communities.txt", "r") as f:
#     try:
#         data = json.load(f)
#     # if the file is empty the ValueError will be thrown
#     except ValueError:
#         data = {} 