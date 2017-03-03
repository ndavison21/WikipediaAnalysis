print "Importing Libraries"

import networkx as nx
from multiprocessing import Pool
import sys
import random
from collections import deque


print "Reading in Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_rw.txt', create_using=nx.DiGraph(), nodetype=int)


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

p = Pool()
num_partitions = len(p._pool)
size_partitions = 10000 / num_partitions

print num_partitions, "partitions of size", size_partitions
sys.stdout.flush()

partitions = list()
for i in range(0, num_partitions):
	partitions.append(random.sample(g.nodes(), size_partitions))

print num_partitions, "partitions."
sys.stdout.flush()


dists = p.map(separation, partitions)

print "Complete. Writing to file."
sys.stdout.flush()

dist = dists[0]
for hist in dists:
	for n in hist:
		if n in dist:
			dist[n] += hist[n]
		else:
			dist[n] = hist[n]

with open("results/separation_10000_parallel.txt", "w+") as file:
	for key,value in dist.iteritems():
		file.write("{} {}\n".format(key, value))
	file.close()

p = Pool()
num_partitions = len(p._pool)
size_partitions = 100000 / num_partitions

print num_partitions, "partitions of size", size_partitions
sys.stdout.flush()

partitions = list()
for i in range(0, num_partitions):
	partitions.append(random.sample(g.nodes(), size_partitions))

print num_partitions, "partitions."
sys.stdout.flush()


dists = p.map(separation, partitions)

print "Complete. Writing to file."
sys.stdout.flush()

dist = dists[0]
for hist in dists:
	for n in hist:
		if n in dist:
			dist[n] += hist[n]
		else:
			dist[n] = hist[n]

with open("results/separation_100000_parallel.txt", "w+") as file:
	for key,value in dist.iteritems():
		file.write("{} {}\n".format(key, value))
	file.close()

print "we done here"
