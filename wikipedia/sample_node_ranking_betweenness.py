print "Importing Libraries"

import networkx as nx
from multiprocessing import Pool, freeze_support
import itertools
import sys

print "Reading in Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_rw.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."
sys.stdout.flush()

def get_top_keys(dictionary, top):
    min_node = -1
    min_value = sys.maxint
    top = dict()
    for (n, b) in dictionary.iteritems():
        if len(top) < 20:
            top[n] = b
            if b < min_value:
                min_node = n
                min_value = b
        elif b > min_value:
            del top[min_node]
            top[n] = b
            min_value = sys.maxint
            for (m, c) in top.iteritems():
                if c < min_value:
                    min_node = m
                    min_value = c

    items = sorted(top.iteritems(), key=lambda (k,v): (v,k), reverse=True)

    return items

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
    print p._pool
    sys.stdout.flush()
    part_generator = 4*len(p._pool)
    node_partitions = list(partitions(G.nodes(), int(len(G)/part_generator)))
    num_partitions = len(node_partitions)
 
    print "Partitions:", num_partitions
    sys.stdout.flush()
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


if __name__ == '__main__':
    freeze_support()

    print "Calculating betweeness"
    sys.stdout.flush()
    bt = between_parallel(g)

    file = open ("results/sample/top20betweenness.txt", "w+")
    file.write("node betweenness\n")

    print "Writing details of betweeness"
    sys.stdout.flush()
    for (node, btwn) in get_top_keys(bt, 20):
        file.write("{} {}\n".format(node,btwn))
