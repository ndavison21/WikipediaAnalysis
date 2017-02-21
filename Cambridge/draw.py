print "Importing Libraries."
import networkx as nx
import matplotlib

matplotlib.use('AGG')

import matplotlib.pyplot as plt

plt.ioff()

with open('spring_pos_50.pickle', 'rb') as handle:
    spring_pos = pickle.load(handle)

print "Drawing Network (Spring)"
plt.axis("off")
nx.draw_spring(g, spring_pos, with_labels = False, node_size = 35)
print "Saving Figure"
plt.savefig('results/cam_spring.pdf')
