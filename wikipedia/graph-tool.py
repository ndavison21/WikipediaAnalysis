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

print "Graph Imported"

pos = gt.sfdp_layout(g)
gt.graph_draw(g, pos, output_size=(1000, 1000), vertex_color=[1,1,1,0], vertex_size=1, edge_pen_width=1.2, output="wiki_1000.png")