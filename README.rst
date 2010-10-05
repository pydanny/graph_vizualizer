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