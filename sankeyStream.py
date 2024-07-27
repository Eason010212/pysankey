import matplotlib.pyplot as plt

class Node:
    def __init__(self, id, label='', color='blue', weight=0, depth=-1):
        self.id = id
        self.label = label
        self.color = color
        self.weight = weight
        self.depth = depth
        self.pos = {
            'x': 0,
            'y': 0
        }

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
        self.plot = None
        
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
        self.plot = plt.figure(figsize=(10, 10))
        ax = plt.gca()
        ax.axis('off')
        maxDepth = max([node.depth for node in self.nodes])
        nodeSpacing = 1.0 / (maxDepth + 1)
        for node in self.nodes:
            node.pos['x'] = node.depth * nodeSpacing
            node.pos['y'] = 0.5
            ax.text(node.pos['x'], node.pos['y'], node.label, ha='center', va='center', color=node.color)
        
        return self

    def display(self):
        plt.show()
        return plt
    
