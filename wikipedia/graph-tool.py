import graph_tool.all as gt
import numpy.random as rand  # for random sampling
rand.seed(42)

g = gt.Graph()
file = open ('data/wiki-Talk_1000.txt', 'r')
edges = file.readlines()

for line in edges:
    edge = line.replace('\r\n','')
    edge = edge.split('	')
    e = g.add_edge(edge[0], edge[1])

print "Number of nodes", g.number_of_nodes()
print "Number of edges", g.number_of_edges()

# for v in g.vertices():
# 	print("vertex:", int(v), "in-degree:", v.in_degree(), "out-degree:", v.out_degree())
# 	if (int(v) == 10):
# 		break

# v = g.vertex(rand.randint(0, g.num_vertices()))
# while True:
#     print("vertex:", int(v), "in-degree:", v.in_degree(), "out-degree:", v.out_degree())

#     if v.out_degree() == 0:
#         print("Nowhere else to go... We found the main hub!")
#         break

#     n_list = []
#     for w in v.out_neighbours():
#         n_list.append(w)
#     v = n_list[randint(0, len(n_list))]