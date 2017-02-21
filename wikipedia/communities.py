import sys
print "Importing Libraries"
sys.stdout.flush()
import networkx as nx
import community
import matplotlib

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

print "Writing to file."
sys.stdout.flush()
with open('communities_100.pickle', 'wb+') as handle:
    pickle.dump(values, handle, protocol=pickle.HIGHEST_PROTOCOL)

# nx.draw(g, pos=spring_pos, cmap=plt.get_cmap("jet"), node_color=values, with_labels = False, node_size = 100)

print "We done here."