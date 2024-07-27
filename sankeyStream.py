import matplotlib.pyplot as plt

class Node:
    def __init__(self, id, label='', color='blue', weight=0, depth=-1):
        self.id = id
        self.label = label
        self.color = color
        self.weight = weight
        self.depth = depth

class Link:
    def __init__(self, source, target, value=0):
        self.source = source
        self.target = target
        self.value = value

class Sankey:
    def __init__(self, nodes=[], links=[], orientation='h'):
        self.nodes = nodes
        self.links = links
        self.orientation = orientation
        self.plot = plt.figure()
        
    def add_node(self, id, **attr):
        node = Node(id, **attr)
        self.nodes.append(node)
        return node
    
    def add_link(self, source, target, **attr):
        if isinstance(source, Node): source = source.id
        if isinstance(target, Node): target = target.id
        link = Link(source, target, **attr)
        self.links.append(link)
        return link
    
    def draw(self):
        if self.orientation == 'h':
            return self.draw_h()
        elif self.orientation == 'v':
            return self.draw_v()
        elif self.orientation == 'o':
            return self.draw_o()
        else:
            raise ValueError('orientation should be h, v, or o')
    
    def draw_h(self):
        ax = self.plot.add_subplot(1, 1, 1, xticks=[], yticks=[], title='Sankey Diagram')
        y = [0]
        for i, node in enumerate(self.nodes):
            node.depth = i
            ax.text(0, y[-1], node.label, ha='center', va='center')
            y.append(y[-1] - node.weight)
        for link in self.links:
            source = self.nodes[link.source]
            target = self.nodes[link.target]
            ax.plot([0, 1], [y[source.depth], y[target.depth]], color='black')
        return self

    def display(self):
        plt.show()
        return plt
    
