print "Importing Libraries"
import sys
import networkx as nx
import random

print "Reading in Full Graph"
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)


i=0
failed = 0
nodes = random.sample(g.nodes(), 8000)
distribution = dict()
for src in nodes:
	print "No path to", failed, "nodes"
	print "Node", i, ":", src
	sys.stdout.flush()
	failed = 0
	i = i + 1
	for dest in random.sample(g.nodes(), 100000):
		try:
			l = nx.shortest_path_length(g, src, dest)
			if l in distribution:
				distribution[l] = distribution[l] + 1
			else:
				distribution[l] = 1
		except nx.NetworkXNoPath:
			failed = failed + 1
			continue
	if i == 1000:
		print "1000 done"
		sys.stdout.flush()
		with open("results/separation_1000.txt", "w+") as file:
			for key,value in distribution.iteritems():
				file.write("{} {}\n".format(key, value))
			file.close()
	elif i == 3000:
		print "3000 done"
		sys.stdout.flush()
		with open("results/separation_3000.txt", "w+") as file:
			for key,value in distribution.iteritems():
				file.write("{} {}\n".format(key, value))
			file.close()

with open("results/separation_8000.txt", "w+") as file:
	for key,value in distribution.iteritems():
		file.write("{} {}\n".format(key, value))
	file.close()

print "We Done Here."
