print "Importing Libraries"
import sys
import networkx as nx
import random

print "Reading in Full Graph"
sys.stdout.flush()
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)


i=0
nodes = random.sample(g.nodes(), 80)
distribution = dict()
for src in nodes:
	i = i + 1
	for dest in g.nodes():
		try:
			l = nx.shortest_path_length(g, src, dest)
			if l in distribution:
				distribution[l] = distribution[l] + 1
			else:
				distribution[l] = 1
		except nx.NetworkXNoPath:
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
