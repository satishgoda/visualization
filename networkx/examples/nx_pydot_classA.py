## imports
import os
from PIL import Image

import pydot
import networkx as nx

## class definition

class A(object):
    def __init__(self, name):
        self.name = name

## class instantiation

a1 = A('A a1')
a2 = A('A a2')

## nx DiGraph initialization

dg = nx.DiGraph(name="nx DiGraph example")

## add nx DiGraph nodes

dg.add_node(A, label='class {0}'.format(A.__name__))

dg.add_node(a1, label=a1.name)
dg.add_node(a2, label=a2.name)

## nx DiGraph node list

print dg.nodes()

## nx DiGraph node properties

print dg.node[A]

## Modify nx node properties

for node in dg.nodes():
    properties = dg.node[node]
    
    properties['style'] = "filled, bold"
    
    if isinstance(node, type):
        properties['fillcolor'] = 'gray'
    else:
        properties['fillcolor'] = 'lightgray'

## nx DiGraph node properties

print dg.node[A]

## add nx DiGraph edges

dg.add_edge(A, a1)
dg.add_edge(A, a2)

## nx DiGraph all edges

print dg[A]

## nx DiGraph edges

print dg[A][a1]
print dg[A][a2]

## Modify nx edge properties

for fromNode, toNode in dg.edges():
    properties = dg[fromNode][toNode]
    properties['tooltip'] = "Is an instance of"
    properties['penwidth'] = 2.5

## nx DiGraph edges with properties

print dg[A]
print dg[A][a1]
print dg[A][a2]

## Write the nx DiGraph in dot format

dotfilepath = '/srv/scratch/nxgraph.dot'

nx.write_dot(dg, dotfilepath)

## Read dot file in pydot

pydot_graph = pydot.graph_from_dot_file(dotfilepath)
pydot_graph.write_svg(svgfilepath)

## Write png file of dot graph

# pngfilepath = '/srv/scratch/nxgraph.png'
# pydot_graph.write_png(pngfilepath)
# Image.open(pngfilepath).show()

## Write svg file of dot graph

svgfilepath = '/srv/scratch/nxgraph.svg'
pydot_graph.write_svg(svgfilepath)
os.system('firefox {0} &'.format(svgfilepath))
