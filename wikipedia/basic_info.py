print "Importing Libraries"

import networkx as nx

print "Reading in Graph (100)."
g = nx.read_edgelist('data/wiki-Talk_100.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."

print "Need to convert to undirected graph."
g_ud = g.to_undirected()

print "Writing to file"
file = open("results/basic_info_100.txt", "w+")
print "Graph Info."
file.write(nx.info(g))
print "Number of Strongly Connected Components."
file.write("SCC: {}\n".format(nx.number_strongly_connected_components(g)))
print "Number of Weakly Connected Components."
file.write("WCC: {}\n".format(nx.number_weakly_connected_components(g)))
print "Average Clustering Coefficient."
file.write("Average Clustering Coefficient: {}\n".format(nx.average_clustering(g_ud)))
print "Largest Connected Component"
conn = max(nx.connected_component_subgraphs(g_ud), key=len)
file.write("Largest Connected Component")
file.write(nx.info(g))
print "Average Path Length in Connected Component"
pl = nx.average_shortest_path_length(conn)
print pl
file.write("Avg Shortest Path Length: {}\n").format(pl)
print "Average Clustering in Connected Component"
clus = nx.average_clustering(conn)
print clus
file.write("Avg Shortest Path Length: {}\n").format(clus)
file.close()

print "We Done Here."
sys.stdout.flush()
