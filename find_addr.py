import xml.etree.ElementTree as ET
import gzip

def search_addr(search_housenumber, search_street):
    search_housenumber = search_housenumber.strip().lower()
    search_street = search_street.strip().lower()
    found = set()
    for i in range(1, 30):
        filename = f'tracts/tract{i:02d}.osm.gz'
        input_file = gzip.open(filename, 'r')
        tree = ET.parse(input_file)
        root = tree.getroot()
        
        for node in root:
            housenumber = ''
            street = ''
            unit = ''
            city = ''
            for tag in node:
                #for name, value in tag.attrib.items():
                #    print(filename)
                #    print('{0}="{1}"'.format(name, value))
                key = tag.attrib['k']
                value = tag.attrib['v']
                if key == 'addr:housenumber':
                    housenumber = value.strip().lower()
                if key == 'addr:street':
                    street = value.strip().lower()
                if key == 'addr:city':
                    city = value.strip().lower()
                if key == 'addr:unit':
                    unit = value.strip().lower()
            if housenumber == search_housenumber and street == search_street:
                found.add(filename)
    return list(found)

def main():
    housenumber_input = input('Enter housenumber:')
    street_input = input('Enter street:')

    housenumber_input = housenumber_input.strip().lower()
    street_input = street_input.strip().lower()
    found_files = search_addr(housenumber_input, street_input)
    print('Found in file(s): ' + ', '.join(found_files))
    

if __name__ == '__main__':
    main()