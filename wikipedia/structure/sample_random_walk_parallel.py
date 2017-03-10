import networkx as nx
from multiprocessing import Pool
import sys
import random as rand

print "Reading Graph"
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)


def random_walk(args):
	(limit, p, partition_target_nodes) = args
	g_sample = nx.Graph()
	steps = 0

	finished = False
	while not(finished):
		source = rand.choice(g.nodes())
		node = source
		steps = 0
		while(steps < limit):
			steps = steps + 1
			if rand.random() < p:
				node = source
			nodes = g.neighbors(node)
			if (len(nodes) == 0):
				continue
			next_node = rand.choice(nodes)
			if not(g_sample.has_edge(node, next_node)):
				g_sample.add_edge(node, next_node)
				steps = 0
				node = next_node
				if nx.number_of_nodes(g_sample) >= partition_target_nodes:
					finished = True
					break
			if (steps >= limit):
				print "Steps Limit Reached. Sample has", nx.number_of_nodes(g_sample), "nodes. Target:", target_nodes
				sys.stdout.flush()
	return g_sample


target_nodes = 0.15 * nx.number_of_nodes(g)

print "Target Nodes:", target_nodes
sys.stdout.flush()
p = 0.15
limit = nx.number_of_nodes(g)

pool = Pool()
num_partitions = len(pool._pool)
partition_target_nodes = target_nodes / num_partitions


samples = pool.map(random_walk, [(limit,p,partition_target_nodes)]*num_partitions)

print "Sample done, writing to file."
sys.stdout.flush()



g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
file = open("data/wiki-Talk_rw_leng_parallel.txt", "w+")
for g_sample in samples:
	for u, v in g_sample.edges_iter():
		if g.has_edge(u, v):
			file.write("{} {}\n".format(u, v))
		if g.has_edge(v, u):
			file.write("{} {}\n".format(v, u))
file.close()

