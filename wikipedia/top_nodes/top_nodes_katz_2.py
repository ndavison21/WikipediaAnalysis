import networkx as nx
from sys import stdout

def katz_centrality_iter(G, alpha=0.1, beta=1.0,
                    max_iter=1000, tol=1.0e-6, nstart=None, normalized=True,
                    weight = 'weight'):
    from math import sqrt

    if len(G) == 0:
        return {}

    nnodes = G.number_of_nodes()

    if nstart is None:
        # choose starting vector with entries of 0
        x = dict([(n,0) for n in G])
    else:
        x = nstart

    try:
        b = dict.fromkeys(G,float(beta))
    except (TypeError,ValueError,AttributeError):
        b = beta
        if set(beta) != set(G):
            raise nx.NetworkXError('beta dictionary '
                                   'must have a value for every node')

    # make up to max_iter iterations
    for i in range(max_iter):
    	print i
    	stdout.flush()
        xlast = x
        x = dict.fromkeys(xlast, 0)
        # do the multiplication y^T = Alpha * x^T A - Beta
        for n in x:
            for nbr in G[n]:
                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
        for n in x:
            x[n] = alpha*x[n] + b[n]

        # check convergence
        err = sum([abs(x[n]-xlast[n]) for n in x])
        if err < nnodes*tol:
            if normalized:
                # normalize vector
                try:
                    s = 1.0/sqrt(sum(v**2 for v in x.values()))
                # this should never be zero?
                except ZeroDivisionError:
                    s = 1.0
            else:
                s = 1
            for n in x:
                x[n] *= s
            return x

    print 'Power iteration failed to converge in %d iterations.' % max_iter
    stdout.flush()
    return x

def get_top_keys(dictionary, top):
    items = dictionary.items()
    items.sort(reverse=True, key=lambda x: x[1])
    return items[:top]

print "Reading in Full Graph."
stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)

print "Katz 2."
stdout.flush()


katz = katz_centrality_iter(g, max_iter=100000)



file = open("results/katz.txt", "w+")
file.write("Top 100 Nodes by katz centrality\n")
for node in get_top_keys(katz, 100):
    file.write("{}, {}\n".format(node[0], node[1]))
file.close()

print "We Done Here."
