====================
Graph Vizualizer
====================

Accepts a CSV and turns it into a Node map. Renders via Graphviz into several formats

CSV input format
----------------

Each line represents a node. Nodes can have shapes and and styles. Node names that are too
    long are wrapped for convenience. Node elements are:
    
    1. name
        string: anything - duplicates no allowed!
    2. shape
        string: box, ellipse, circle, diamond, octogon, rect, folder
    3. style    
        string: default
    4. going to (arrow points away from node) 
        comma delineated list, case insensitive, duplicates are removed
    5. coming from (arrow points to node)
        comma delineated list, case insensitive, duplicates are removed
        
usage
-----

At the command-line::

    python vizualizer.py -c test_data/basic_test.csv
    
For now it will print the graph notation to the terminal. Will be using graphviz itself to render the image.

TODO
----

 * plug in graphviz notation
 * combine a -- b and b -- a edges into one edge notated as bidirectional
 * add in directional arrows
 * possible CSV header control
 * styling system (backgrounds and text color)
