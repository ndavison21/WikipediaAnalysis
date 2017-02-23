import sys
print "Importing Libraries"
sys.stdout.flush()
import networkx as nx
from multiprocessing import Pool
import itertools
import pickle

print "Reading in Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_rw.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."
sys.stdout.flush()

def partitions(nodes, n):
    print "Partition the nodes into n subsets"
    nodes_iter = iter(nodes)
    while True:
        partition = tuple(itertools.islice(nodes_iter,n))
        if not partition:
            return
        yield partition

def btwn_pool(G_tuple):
    return nx.betweenness_centrality_source(*G_tuple)

def between_parallel(G, processes = None):
    p = Pool(processes=processes)
    part_generator = 4*len(p._pool)
    node_partitions = list(partitions(G.nodes(), int(len(G)/part_generator)))
    num_partitions = len(node_partitions)
 
    bet_map = p.map(btwn_pool,
                        zip([G]*num_partitions,
                        [True]*num_partitions,
                        [None]*num_partitions,
                        node_partitions))
 
    bt_c = bet_map[0]
    for bt in bet_map[1:]:
        for n in bt:
            bt_c[n] += bt[n]
    return bt_c


print "Calculating betweenness"
sys.stdout.flush()
bt = between_parallel(g)
top = 10

max_nodes =  sorted(bt.iteritems(), key = lambda v: -v[1])[:top]
bt_values = [5]*len(g.nodes())
bt_colors = [0]*len(g.nodes())
for max_key, max_val in max_nodes:
    bt_values[max_key] = 150
    bt_colors[max_key] = 2

print "Storing to file"
sys.stdout.flush()
with open('betweenness_colours_100.pickle', 'wb+') as handle:
    pickle.dump(bt_colors, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('betweenness_values_100.pickle', 'wb+') as handle:
    pickle.dump(bt_values, handle, protocol=pickle.HIGHEST_PROTOCOL)
  

def get_top_keys(dictionary, 10):
    items = dictionary.items()
    items.sort(reverse=True, key= lambda x: x[1])
    return map(lambda x: x[0], items[:top])

top_100_btwn = open('top_100_betweeness_nodes.txt', 'wb+')
for node in get_top_keys(bt, 100):
    top_100_btwn.write(node)

# print "Drawing Network."
# plt.axis("off")
# nx.draw_networkx(g, cmap = plt.get_cmap("rainbow"), node_color = bt_colors, node_size = bt_values, with_labels = False)

print "We done here."
sys.stdout.flush()
