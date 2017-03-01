print "Importing Libraries"
import sys
import networkx as nx

print "Reading in Giant Component"
sys.stdout.flush()
g = nx.read_edgelist('data/sample_giant_component.txt', create_using=nx.Graph(), nodetype=int)
print "Fing All Pairs Shortest Path Lengths"
sys.stdout.flush()
shortest_path_lengths = nx.all_pairs_shortest_path_length(g)
path_lengths = sorted(set(in_degrees.values()))
print "Generating Histogram"
sys.stdout.flush()
path_length_hist = [in_degrees.values().count(x) for x in path_lengths]

print "Drawing Path Length Distribution"
plt.figure()
plt.grid(True)
plt.plot(path_lengths, path_length_hist, 'ro-')
plt.xlabel('Path Length')
plt.ylabel('Number of Pairs')
plt.title('Wikipedia Talk Network')
plt.xlim([0, max_degree])
plt.savefig('results/sample_path_length_distribution.pdf')
plt.close()