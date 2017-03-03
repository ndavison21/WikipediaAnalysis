print "Importing Libraries"

import networkx as nx
from multiprocessing import Pool
import sys
import random


print "Reading in Graph."
sys.stdout.flush()
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)


def separation(sources):
	distribution = dict()
	for src in sources:
		print "source: ", src
		sys.stdout.flush()
		for dest in g.nodes():
			try:
				l = nx.shortest_path_length(g, src, dest)
				if l in distribution:
					distribution[l] = distribution[l] + 1
				else:
					distribution[l] = 1
			except nx.NetworkXNoPath:
				continue
	return distribution

p = Pool()
num_partitions = len(p._pool)
size_partitions = 80 / num_partitions

print num_partitions, "partitions of size", size_partitions
sys.stdout.flush()

partitions = list()
for i in range(0, num_partitions):
	partitions.append(random.sample(g.nodes(), size_partitions))

print num_partitions, "partitioned."
sys.stdout.flush()


dists = p.map(separation, partitions)

print "Complete. Writing to file."
sys.stdout.flush()

dist = dists[0]
for hist in dists:
	print hist
	for n in hist:
		if n in dist:
			dist[n] += hist[n]
		else:
			dist[n] = hist[n]

with open("results/separation_8000_parallel.txt", "w+") as file:
	for key,value in dist.iteritems():
		file.write("{} {}\n".format(key, value))
	file.close()
