import sys
print "Importing Libraries."
sys.stdout.flush()
import networkx as nx
import pickle


print "Reading in 100 Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_rw.txt', create_using=nx.DiGraph(), nodetype=int)

print "Drawing Network (rw, 100 iterations)"
sys.stdout.flush()
spring_pos = nx.spring_layout(g, iterations = 100)
print "Saving Positions"
sys.stdout.flush()
with open('spring_pos_rw.pickle', 'wb+') as handle:
    pickle.dump(spring_pos, handle, protocol=pickle.HIGHEST_PROTOCOL)


# with open('filename.pickle', 'rb') as handle:
#     b = pickle.load(handle)
