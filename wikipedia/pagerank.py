import sys
print "Importing Libraries"
sys.stdout.flush()
import networkx as nx
import pickle

print "Reading in Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."
sys.stdout.flush()


print "Calculating PageRank"
sys.stdout.flush()
pagerank = nx.pagerank_numpy(g)

print "Storing to file"
sys.stdout.flush()
with open('pagerank.pickle', 'wb+') as handle:
    pickle.dump(pagerank, handle, protocol=pickle.HIGHEST_PROTOCOL)

def get_top_keys(dictionary, 10):
    items = dictionary.items()
    items.sort(reverse=True, key= lambda x: x[1])
    return map(lambda x: x[0], items[:top])

top_100_btwn = open('top_100_pagerank_nodes.txt', 'wb+')
for node in get_top_keys(pagerank, 100):
    top_100_btwn.write(node)  

# print "Drawing Network."
# plt.axis("off")
# nx.draw_networkx(g, cmap = plt.get_cmap("rainbow"), node_color = bt_colors, node_size = bt_values, with_labels = False)

print "We done here."
sys.stdout.flush()
