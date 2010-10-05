import csv
from elements import Node, Graph
from settings import LEGAL_OUTPUTS

def open_csv(csv_file):
    rows = []
    records = csv.reader(open(csv_file, 'r'))
    for i, record in enumerate(records):    
        if i == 0: 
            # we always skip the header
            continue
        if not record[0]:
            # empty record so skip
            continue
        rows.append(record)
    return rows

def main(csv_file, output):
    
    graph = Graph()
    records = csv.reader(open(csv_file, 'r'))
    for record in open_csv(csv_file):
        graph.add_node(record[0], record[1], record[2], record[3], record[4])

    # TODO - get this to work directly with graphviz rather than a screen print
    print graph.render()

if __name__ == '__main__':
    
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-c', '--csv', dest="csv_file", action="store", help="CSV file to process")
    parser.add_option('-o', '--output ', dest="output", action="store", help="Output file. Extension determines which format to use. Legal formats are .jpg, .png, and .svg")    
    (options, args) = parser.parse_args()

    if not options.csv_file:
        parser.error("option -c is required! Please provide a target csv file to process!")
    
    """
    # TODO - get this working with graphviz directly
    if not options.output:
        parser.error("option -o is required! Please provide an output file target!")
        
    for op in LEGAL_OUTPUTS:
        if options.output.endswith(op):
            break
    else:
        parser.error('For option -o please end the file with one of: %s' % ','.join(LEGAL_OUTPUTS))
    """
    
    main(options.csv_file, options.output)