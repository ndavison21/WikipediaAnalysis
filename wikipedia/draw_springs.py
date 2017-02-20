import sys
print "Importing Libraries."
sys.stdout.flush()
import networkx as nx
import matplotlib

matplotlib.use('AGG')

import matplotlib.pyplot as plt

plt.ioff()

print "Reading in 10,000 Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_10000.txt', create_using=nx.DiGraph(), nodetype=int)

print "Drawing Network (Spring)"
sys.stdout.flush()
plt.figure(num=None, figsize=(10, 10), dpi = 1200)
plt.axis("off")
spring_pos = nx.spring_layout(g, iterations = 20)
nx.draw(g, pos=spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
sys.stdout.flush()
plt.savefig('results/wiki_10000_spring.pdf')

print "Reading in 1,000 Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_1000.txt', create_using=nx.DiGraph(), nodetype=int)

print "Drawing Network (Spring)"
sys.stdout.flush()
plt.figure(num=None, figsize=(10, 10), dpi = 1200)
plt.axis("off")
spring_pos = nx.spring_layout(g, iterations = 20)
nx.draw(g, pos=spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
sys.stdout.flush()
plt.savefig('results/wiki_1000_spring.pdf')


print "Reading in 100 Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_100.txt', create_using=nx.DiGraph(), nodetype=int)

print "Drawing Network (Spring)"
sys.stdout.flush()
plt.figure(num=None, figsize=(10, 10), dpi = 1200)
plt.axis("off")
spring_pos = nx.spring_layout(g, iterations = 20)
nx.draw(g, pos=spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
sys.stdout.flush()
plt.savefig('results/wiki_100_spring.pdf')


print "Reading in 10 Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_10.txt', create_using=nx.DiGraph(), nodetype=int)

print "Drawing Network (Spring)"
sys.stdout.flush()
plt.figure(num=None, figsize=(10, 10), dpi = 1200)
plt.axis("off")
spring_pos = nx.spring_layout(g, iterations = 20)
nx.draw(g, pos=spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
sys.stdout.flush()
plt.savefig('results/wiki_10_spring.pdf')