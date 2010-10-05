import unittest

from elements import Node, Graph, DuplicateNode, InvalidShape, InvalidStyle
from vizualizer import open_csv

class TestGraph(unittest.TestCase):
    
    def test_add(self):
        
        records = open_csv('test_data/basic_test.csv')
        self.assertEquals(2, len(records))
        
    def test_dupes(self):
        
        graph = Graph()
        node = Node('alpha','box','basic')
        graph.add_node(node)
        self.assertRaises(DuplicateNode, graph.add_node, node)               
        
    def test_bad_shape(self):

        self.assertRaises(InvalidShape, Node, 'alpha', 'hoop', 'basic')               

    def test_bad_style(self):

        self.assertRaises(InvalidStyle, Node, 'alpha', 'box', 'disco')               



if __name__ == "__main__":
    unittest.main()