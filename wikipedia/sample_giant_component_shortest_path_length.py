print "Importing Libraries"
import sys
import networkx as nx

print "Reading in Giant Component"
sys.stdout.flush()
g = nx.read_edgelist('data/sample_giant_component.txt', create_using=nx.Graph(), nodetype=int)

file = open("results/sample/giant_component.txt", "w+")
file.write(g.info)
file.flush()

print "\nFinding All Pairs Shortest Path Lengths"
sys.stdout.flush()
shortest_path_lengths = nx.all_pairs_shortest_path_length(g)
path_lengths = sorted(set(shortest_path_lengths.values()))
print "Generating Histogram"
sys.stdout.flush()
path_length_hist = [in_degrees.values().count(x) for x in path_lengths]

file.write("\nDiameter: {}\n".format(path_lengths[-1]))
file.close()


print "Drawing Path Length Distribution"
sys.stdout.flush()
plt.figure()
plt.grid(True)
plt.plot(path_lengths, path_length_hist, 'ro-')
plt.xlabel('Path Length')
plt.ylabel('Number of Paths')
plt.title('Wikipedia Talk Network')
plt.xlim([0, max_degree])
plt.savefig('results/sample_path_length_distribution.pdf')
plt.close()
