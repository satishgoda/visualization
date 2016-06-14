import webbrowser

import networkx as nx
import pydot
from PIL import Image

##
nxdg = nx.DiGraph()

nxdg.add_node('N1')
nxdg.add_node('N2')
nxdg.add_node('A1')
nxdg.add_node('A2')
nxdg.add_node('S1')
nxdg.add_node('M1')
nxdg.add_node('D1')
##
nxdg.add_edge('N1', 'A1')
nxdg.add_edge('N1', 'A2')
nxdg.add_edge('N2', 'A2')
nxdg.add_edge('A1', 'S1')
nxdg.add_edge('N1', 'S1')
nxdg.add_edge('A1', 'M1')
nxdg.add_edge('A2', 'M1')
nxdg.add_edge('S1', 'D1')
nxdg.add_edge('M1', 'D1')

nx.drawing.nx_pydot.write_dot(nxdg, "C:\\tmp\\nx.dot")

g = pydot.graph_from_dot_file("C:\\tmp\\nx.dot")

imageFileName = "C:\\tmp\\nx.svg"

g.write_svg(imageFileName)

webbrowser.open(imageFileName)
