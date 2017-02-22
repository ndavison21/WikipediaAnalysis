import sys
import networkx as nx
import random as rand
from numpy import random
from collections import deque

g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)

total_nodes = nx.number_of_nodes(g)
target_nodes = 0.15 * total_nodes

print "Total Nodes:", total_nodes
print "Target Nodes:", target_nodes

print nx.info(g)

to_burn = deque()

finished = False
p = 2.0 / 3.0
print p

sys.stdout.flush()

while not(finished):
    print "Sample has", total_nodes, "nodes. Target:", target_nodes
    to_burn.clear()
    to_burn.append(rand.choice(g.nodes()))

    while to_burn:                
        burning = to_burn.popleft()   
        nodes = g.neighbors(burning)
        g.remove_node(burning)
        
        total_nodes = total_nodes - 1
        if (total_nodes <= target_nodes):        
            finished = True
            break

        nodes = [node for node in nodes if node not in to_burn and not(node == burning)]
        x = random.geometric(p)
        if len(nodes) > x:                   
                nodes = rand.sample(nodes, x)
        to_burn.extend(nodes)


print nx.info(g)

outfile = open("wiki-Talk_ff.txt", "wb+")
nx.write_edgelist(g, outfile)