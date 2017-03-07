from numpy import histogram, log10
import pylab as plt

node_clustering = dict()
clustering_sum = 0

clust_0 = 0
clust_1 = 0

print "Reading in Clusterings"
with open("results/node_clustering.txt", "r") as f:
    for line in f.readlines():
        node, clustering = (line.rstrip('\n')).split(' ')
        node_clustering[(int(node))] = float(clustering)
        clustering_sum += float(clustering)
        if clustering == 0.0:
        	clust_0 += 1
        elif clustering == 1.0:
        	clust_1 += 1

print "Generating Histogram"
hist, bins = histogram(node_clustering.values(), bins=100)

with open("results/avg_clustering.txt", "w+") as f:
	f.write("Average Clustering: {}\n".format(clustering_sum/2394385))

width = 0.7 * (bins[2] - bins[1])
center = (bins[:-1] + bins[1:]) / 2

plt.figure()
plt.grid(True)
plt.bar(center[1:-1], hist[1:-1], align='center', width=width)
plt.xlabel('Clustering Coefficient')
plt.xlim([0, 1])
plt.ylabel('Number of Nodes')
plt.savefig('results/figures/clustering_hist.pdf')
plt.close()

log_hist = list()
for n in hist:
	if n == 0:
		log_hist.append(0)
	else:
		log_hist.append(log10(n))


plt.figure()
plt.grid(True)
plt.bar(center, log_hist, align='center', width=width)
plt.xlabel('Clustering Coefficient')
plt.xlim([0, 1])
plt.ylabel('Number of Nodes (log10)')
plt.savefig('results/figures/clustering_hist_log.pdf')
plt.close()
