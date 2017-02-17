print "Importing Libraries"

import networkx as nx
import pylab as plt
import numpy as np
from scipy import optimize

print "Reading in Graph."
g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported, analysing and plotting node degrees."