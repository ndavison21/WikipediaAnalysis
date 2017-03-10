from networkx import DiGraph, read_edgelist, hits_numpy
from sys import stdout

def get_top_keys(dictionary, top):
	items = dictionary.items()
	items.sort(reverse=True, key=lambda x: x[1])
	return items[:top]

print "Reading in Full Graph."
stdout.flush()
g = read_edgelist('data/wiki-Talk.txt', create_using=DiGraph(), nodetype=int)

print "HITS."
stdout.flush()

hubs,authorities = hits_numpy(g)

file = open("results/hubs_numpy.txt", "w+")
file.write("Top 100 Hubs by HITS\n")
for node in get_top_keys(hubs, 100):
	file.write("{} {}\n".format(node[0], node[1]))
file.close()

file = open("results/authorities_numpy.txt", "w+")
file.write("Top 100 Authorities by HITS\n")
for node in get_top_keys(authorities, 100):
	file.write("{} {}\n".format(node[0], node[1]))
file.close()

print "We Done Here."
