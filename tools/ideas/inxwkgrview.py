##

class GraphWidget(GraphWidgetBase):
    def __init__(self, *args, **kwargs):
        super(GraphWidget, self).__init__(*args, **kwargs)
        self.dg = DiGraph()
    
    def update(self):
        write_dot(self.dg, "F:\wtfrt.dot")
        pdg = graph_from_dot_file("F:\wtfrt.dot")
        pdg.write_svg("F:\wtfrt.svg")
    
        self.load("F:\wtfrt.svg")
    
    def add_edge(self, id1, id2):
        self.dg.add_edge(id1, id2)
        self.update()
    
    def add_node(self, id):
        self.dg.add_node(id)
        self.update()

    def load(self, path):
        svgData = open(path).read()
        self.setHtml(svgData)
        
        wpage = self.page()
        wframe = wpage.mainFrame()
        wdocument = wframe.documentElement()
        svg = wdocument.findFirst('svg')

        for element in svg.findAll('g'):
            if element.attribute('class') == 'node':
                ellipse = element.findFirst('ellipse')
                ellipse.setAttribute('fill', 'white')
                ellipse.setAttribute('stroke-width', '1')
        
    def mousePressEvent(self, evt):
        wframe = self.page().mainFrame()
        element = wframe.hitTestContent(evt.pos()).element()

        print evt.pos(), element.tagName()

        if element.parent().attribute('class') == 'node':
            if element.attribute('fill') == 'white':
                element.setAttribute('fill', 'gray')
            else:
                element.setAttribute('fill', 'white')

        super(GraphWidget, self).mousePressEvent(evt)

##

svgview = GraphWidget()
svgview.show()

##

svgview.add_edge('a', 'b')
svgview.add_edge('a', 'c')
svgview.add_edge('b', 'd')
svgview.add_edge('d', 'a')
svgview.add_node('f')
svgview.add_edge('f', 'g')
svgview.add_edge('b', 'f')
svgview.add_edge('g', 'a')

svgview.add_node('h')
svgview.add_node('i')
svgview.add_node('j')

svgview.findText("j")
svgview.findText("")
svgview.findText("c")
