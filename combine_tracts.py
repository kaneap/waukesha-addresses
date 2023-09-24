
from fileinput import filename
import xml.etree.ElementTree as ET
import gzip

def delete_points(del_points_filename):
    first= None
    for i in range(1, 30):
        filename = f'tracts/tract{i:02d}.osm.gz'
        input_file = gzip.open(filename, 'r')
        tree = ET.parse(input_file)
        data = tree.getroot()
        # print ElementTree.tostring(data)
        if first is None:
            first = data
            first_tree = tree
        else:
            first.extend(data) 
    if first is not None:
        f = gzip.open('combined.osm.gz', 'wb')
        first_tree.write(f) 
        f.close()

def main():
    delete_points('points_to_delete.osm')

if __name__ == '__main__':
    main()