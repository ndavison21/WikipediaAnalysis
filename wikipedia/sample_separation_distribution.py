print "Importing Libraries"
import sys
import networkx as nx

print "Reading in Sample Graph"
g = nx.read_edgelist('data/wiki-Talk_rw.txt', create_using=nx.DiGraph(), nodetype=int)

file = open("results/sample/separation.txt", "w+")
print "Giant Component Info."
file.write("# Graph contains {} nodes\n".format(len(g)))
file.write("# Node, Number of Paths, Average Path Length\n")

i=0
sorted_nodes = sorted(g.nodes())
for node in sorted_nodes[0:]:
	if i % 100 == 0:
		file.flush()
		print i, ": node", node
	path_length = nx.single_source_shortest_path_length(g, node)
	path_length_sum = sum(path_length.values())
	num_paths = len(path_length)
	file.write("{} {} {}\n".format(node, num_paths, float(path_length_sum) / num_paths))
	i = i+1

file.close()
