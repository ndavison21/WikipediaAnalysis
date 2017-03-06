
import networkx as nx
from multiprocessing import Pool
import sys
from collections import deque
from math import floor


print "Reading in Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)


def separation(sources):
	distribution = dict()
	for i in range (0, 21):
		distribution[i] = 0

	for src in sources:
		sys.stdout.flush()

		visited = set()
		nodes_1 = set(g.neighbors(src))
		nodes_2 = set()

		b = True
		i = 0

		while True:
			if  len(nodes_1) == 0:
				break
			i +=1
			distribution[i] += len(nodes_1)
			nodes_2 = set()
			for node in nodes_1:
				if node not in visited:
					visited.add(node)
					nodes_2.update(g.neighbors(node))
			if  len(nodes_2) == 0:
				break
			i += 1
			distribution[i] += len(nodes_2)
			nodes_1 = set()
			for node in nodes_2:
				if node not in visited:
					visited.add(node)
					nodes_1.update(g.neighbors(node))


	return distribution

def partitions(nodes, n):
    nodes_iter = iter(nodes)
    while True:
        partition = tuple(itertools.islice(nodes_iter,n))
        if not partition:
            return
        yield partition

p = Pool()
num_partitions = len(p._pool)
nodes = g.nodes()
size_partitions = int(len(nodes) / num_partitions)

print num_partitions, "partitions of size", size_partitions
sys.stdout.flush()

node_partitions = list(partitions(nodes, size_partitions))

print num_partitions, "partitions."
sys.stdout.flush()


dists = p.imap(separation, node_partitions)

print "Complete. Writing to file."
sys.stdout.flush()

paths = 0
dist = dists[0]
for hist in dists:
	for n in hist:
		paths += hist[n]
		if n in dist:
			dist[n] += hist[n]
		else:
			dist[n] = hist[n]

with open("data/separation_full_parallel.txt", "w+") as file:
	for key,value in dist.iteritems():
		file.write("{} {} {}\n".format(key, value, float(value)/paths))
	file.close()

print "We done here."
