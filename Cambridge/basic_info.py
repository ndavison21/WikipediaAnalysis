print "Importing Libraries"
import sys
import networkx as nx

print "Reading in Sampled Graph."
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)

print "Convert to undirected graph."
sys.stdout.flush()
g_ud = g.to_undirected()

file = open("results/basic_info.txt", "w+")
print "Writing graph info."
file.write(nx.info(g))
print "Writing SCCs."
file.write("SCCs: {}\n".format(nx.number_strongly_connected_components(g)))
print "Writing WCCs."
file.write("WCCs: {}\n".format(nx.number_weakly_connected_components(g)))
print "Writing Average Clustering Coefficient."
file.write("Average Clustering Coefficient: {}\n".format(nx.average_clustering(g_ud)))
sys.stdout.flush()
print "Finding Largest Connected Component"
wiki_components = nx.connected_component_subgraphs(g_ud)
wiki_components_mc = max(wiki_components, key=len)
print "Writing component info."
file.write("Largest Connected Component\n")
file.write(nx.info(g))
print "Writing Average Path Length in Connected Component"
file.write("Avg Shortest Path Length: {}\n".format(nx.average_shortest_path_length(conn)))
print "Writing Average Clustering in Connected Component"
file.write("Avg Clustering: {}\n".format(nx.average_clustering(conn)))
file.close()
sys.stdout.flush()


print "Reading in Full Graph."
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)

print "Convert to undirected graph."
sys.stdout.flush()
g_ud = g.to_undirected()


file = open("results/basic_info_full.txt", "w+")
print "Writing graph info."
file.write(nx.info(g))
print "Writing SCCs."
file.write("SCCs: {}\n".format(nx.number_strongly_connected_components(g)))
print "Writing WCCs."
file.write("WCCs: {}\n".format(nx.number_weakly_connected_components(g)))
print "Writing Average Clustering Coefficient."
file.write("Average Clustering Coefficient: {}\n".format(nx.average_clustering(g_ud)))
sys.stdout.flush()
print "Finding Largest Connected Component"
wiki_components = nx.connected_component_subgraphs(g_ud)
wiki_components_mc = wiki_components[0]
print "Writing component info."
sys.stdout.flush()
file.write("Largest Connected Component\n")
file.write(nx.info(g))
print "Writing Average Path Length in Connected Component"
sys.stdout.flush()
file.write("Avg Shortest Path Length: {}\n".format(nx.average_shortest_path_length(conn)))
print "Writing Average Clustering in Connected Component"
sys.stdout.flush()
file.write("Avg Clustering: {}\n".format(nx.average_clustering(conn)))
file.close()

print "We Done Here."
sys.stdout.flush()
