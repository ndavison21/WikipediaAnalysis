import sys
print "Importing Libraries"
sys.stdout.flush()
import networkx as nx
import pickle

print "Reading in Graph."
sys.stdout.flush()
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."
sys.stdout.flush()


print "Calculating katz centrality"
sys.stdout.flush()
katz = nx.katz_centrality_numpy(g)

print "Storing to file"
sys.stdout.flush()
with open('katz.pickle', 'wb+') as handle:
    pickle.dump(katz, handle, protocol=pickle.HIGHEST_PROTOCOL)

  

# print "Drawing Network."
# plt.axis("off")
# nx.draw_networkx(g, cmap = plt.get_cmap("rainbow"), node_color = bt_colors, node_size = bt_values, with_labels = False)

print "We done here."
sys.stdout.flush()
