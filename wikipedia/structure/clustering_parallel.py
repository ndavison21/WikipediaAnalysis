from multiprocessing import Pool
from itertools import islice
import networkx as nx
from sys import stdout


def chunks(l, n):
    """Divide a list of nodes `l` in `n` chunks"""
    l_c = iter(l)
    while 1:
        x = tuple(islice(l_c, n))
        if not x:
            return
        yield x


def _clustmap(G_normalized_weight_sources_tuple):
    """Pool for multiprocess only accepts functions with one argument.
    This function uses a tuple as its only argument. We use a named tuple for
    python 3 compatibility, and then unpack it when we send it to
    `betweenness_centrality_source`
    """
    return nx.clustering(*G_normalized_weight_sources_tuple)


def clustering_parallel(G, processes=None):
    """Parallel clustering  function"""
    p = Pool(processes=processes)
    node_divisor = len(p._pool)*4
    node_chunks = list(chunks(G.nodes(), int(G.order()/node_divisor)))
    num_chunks = len(node_chunks)
    cl_sc = p.map(_clustmap,
                  zip([G]*num_chunks,
                      node_chunks,
                      [None]*num_chunks))

    # Reduce the partial solutions
    cl_c = cl_sc[0]
    for cl in cl_sc[1:]:
        for n in cl:
            cl_c[n] += cl[n]
    return cl_c

if __name__ == "__main__":
    print "Reading in Graph"
    stdout.flush()
    g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)

    print("Computing clustering for:")
    print(nx.info(g))
    print("Parallel version")
    stdout.flush()
    cl = clustering_parallel(g)

    with open("results/node_clustering.txt", "w+") as file:
        for n, b in bt.iteritems():
            file.write("{} {}\n".format(n, b))

    print "We Done Here."
