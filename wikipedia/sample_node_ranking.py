print "Importing Libraries"
import sys
import networkx as nx

def get_top_keys(dictionary, top):
	items = dictionary.items()
	items.sort(reverse=True, key=lambda x: x[1])
	return items[:top]

g = nx.read_edgelist('data/sample_giant_component.txt', create_using=nx.Graph(), nodetype=int)

file = open("results/sample/ranking_nodes.txt", "w+")

print "Ranking Nodes"
file.write("\n*** RANKING NODES ***\n")
# file.write("Top 20 nodes by In-Edits\n")
# print "In-Edits."
# sys.stdout.flush()
# in_degree_centrality = nx.in_degree_centrality(g)
# file.write("Node ID, Centrality\n")
# for node in get_top_keys(in_degree_centrality, 20):
# 	file.write("{}, {}\n".format(node[0], node[1]))
# file.flush()

print "Betweenness."
sys.stdout.flush()
file.write("\nTop 20 Nodes by Betweenness\n")
betweenness_centrality = nx.betweenness_centrality(g)
for node in get_top_keys(betweenness_centrality, 20):
	file.write("{}, {}\n".format(node[0], node[1]))
file.flush()

print "Katz."
sys.stdout.flush()
file.write("\nTop 20 Nodes by Katz\n")
katz_centrality = nx.katz_centrality_numpy(g)
for node in get_top_keys(katz_centrality, 20):
	file.write("{}, {}\n".format(node[0], node[1]))
file.flush()

print "PageRank."
sys.stdout.flush()
file.write("\nTop 20 Nodes by PageRank\n")
pagerank = nx.pagerank_numpy(g)
for node in get_top_keys(pagerank, 20):
	file.write("{}, {}\n".format(node[0], node[1]))
file.flush()

print "HITS."
sys.stdout.flush()
file.write("\nTop 20 Nodes by HITS: Hubs\n")
hits = nx.hits_numpy(g)
for node in get_top_keys(hits[0], 20):
	file.write("{}, {}\n".format(node[0], node[1]))
file.flush()
file.write("Top 20 Nodes by HITS: Authorities\n")
pagerank = nx.hits_numpy(g)
for node in get_top_keys(hits[1], 20):
	file.write("{}, {}\n".format(node[0], node[1]))

file.close()

print "We Done Here."
sys.stdout.flush()
