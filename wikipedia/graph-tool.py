from graph_tool.all import *

g = gt.Graph()
file = open ('data/wiki-Talk_10000.txt', 'r')
edges = file.readlines()

for line in edges:
    edge = line.replace('\r\n','')
    edge = edge.split('	')
    e = g.add_edge(edge[0], edge[1])