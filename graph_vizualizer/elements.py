import hashlib

from settings import SHAPES, STYLES, UNNODE_SHAPE


class DuplicateNode(Exception):
    pass
    
class InvalidShape(Exception):
    pass
    
class InvalidStyle(Exception):
    pass 
    
def indexifier(name):
    return '_%s' % hashlib.md5(name.lower().replace(' ','')).hexdigest() 
    
def edgifier(node, target):
    return '%s -- %s;' % (node.index, indexifier(target))
    
def render_unnode(name):
    return '%s [label="%s" shape="%s"];' % (indexifier(name), name, UNNODE_SHAPE)    
    
    
class Node(object):
    
    def __init__(self, name, shape='box', style='basic', going_to='', coming_from=''):
        
        self.name = name
        self._shape = '' 
        self._style = ''
        self._going_to = ''
        self._coming_from = ''
        
        self.shape = shape
        self.style = style        
        self.going_to = going_to 
        self.coming_from = coming_from       
        
        # Since this is not for security use MD5 cause its shorter and easier to read
        self.index = indexifier(name)
        
    def clean_edges(self, text):
        """
        Splits the edges, removes dupes, and turns it into a list
        """
        return list(set([x.strip() for x in text.split(',')]))
        
    def __repr__(self):
        return "<Node object %s aka %s>" % (self.name, self.index)
        
    @property
    def shape(self):
        return self._shape
        
    @shape.setter
    def shape(self, text):
        if text not in SHAPES:
            raise InvalidShape('Valid shapes are: %s' % ','.join(SHAPES))
        self._shape = text
        
    @property
    def style(self):
        return self._style
        
    @style.setter
    def style(self, text):
        if text not in STYLES:        
            raise InvalidStyle('Valid styles are: %s' % ','.join(STYLES))
            
    @property
    def going_to(self):        
        return self._going_to
        
    @going_to.setter
    def going_to(self, text):
        self._going_to = self.clean_edges(text)

    @property
    def coming_from(self):
        return self._coming_from

    @coming_from.setter
    def coming_from(self, text):        
        self._coming_from = self.clean_edges(text)
        
    def render(self):
        return '%s [label="%s" shape="%s"];' % (self.index, self.name, self.shape)

class Graph(object):
    
    def __init__(self, name='Graph'):
        
        self.name = name
        self.nodes = []
        self.nodes_index = []
        
    def get_node_by_index(self, index):
        """ returns the node or a None object"""
        
        try:
            return self.nodes[self.nodes_index.index(index)]
        except ValueError:
            return None
        
    def get_node_by_name(self, name):
        """ returns the node or a None object"""
        return self.get_node_by_index(indexifier(name))
        
    def node_exists(self, node):
        return node.index in [x.index for x in self.nodes]
        
    def _get_node(self, node):
        """ utility to get old node when being modified 
            relies on the index so we don't lose the node if there is a name change
        """
        return self.nodes[self.nodes_index.index(node.index)]
        
    def add_node(self, node_name, shape='', style='', going_to='', coming_from=''):
        """ accepts Nodes or elements needed to become a node
            returns the node just to be handy
        """
        if isinstance(node_name, str):
            # build the node
            node = Node(node_name, shape, style, going_to, coming_from)
        else:
            # point at the right node name
            node = node_name
        
        if self.node_exists(node):
            raise DuplicateNode("Node '%s' is duplicated. Please check your input CSV" % node.name)
    
        self.nodes.append(node)
        self.nodes_index = [x.index for x in self.nodes]
        return node
                        
    def render(self):
        """
        prints out in graphviz
            # add in unstored items lacking a node
        """
        going_to = set([])
        coming_from = set([])   
        unnodes = set([])
        text = ''     
        for node in self.nodes:
            text += node.render()
            text += '\n'
            for gt in node.going_to:
                if not self.get_node_by_name(gt):
                    unnodes.add(gt)
                edge = edgifier(node, gt)
                going_to.add(edge)
            for cf in node.coming_from:
                if not self.get_node_by_name(cf):
                    unnodes.add(cf)                
                edge = edgifier(node, cf)
                coming_from.add(edge)
        edges = going_to.union(coming_from)
        for edge in edges:
            text += edge
            text += '\n'      
        for node in unnodes:
            text += render_unnode(node)
            text += '\n'      
        
        return 'graph {\n %s }' % text
                
        
        