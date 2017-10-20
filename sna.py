import networkx as nx
import matplotlib as mat
import matplotlib.pyplot as plt

g = nx.Graph()

#adding nodes
g.add_node('George')
g.add_nodes_from(range(1,10))

#adding edges
g.add_edge(5,100)

nx.draw(g, with_labels=True)
plt.draw()
plt.show()
