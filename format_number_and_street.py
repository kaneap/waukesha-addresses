import xml.etree.ElementTree as ET
import simpleaddress

def main():
    tree = ET.parse('source_points.osm')
    root = tree.getroot()
    for node in root:
        number_and_street = ''
        post_office = ''
        has_osm_addr = False
        for tag in node:
            key = tag.attrib['k']
            value = tag.attrib['v']
            if key == 'Full_Address':
                number_and_street = value
            elif key == 'PostOffice':
                post_office = value
            elif key in ('addr:housenumber', 'addr:street', 'addr:city'):
                has_osm_addr = True

        house_number = number_and_street.split(' ')[0]
        street = ''
        if len(number_and_street.split(' ')) > 1:
            street = ' '.join(number_and_street.split(' ')[1:])
            street = street.title()
            street = simpleaddress.normalize(street)
            street = simpleaddress.expand_streetname(street)
            
        city = post_office.title()

        if house_number and street and city and not has_osm_addr:
            house_number_tag = ET.SubElement(node, 'tag')
            house_number_tag.set('k', 'addr:housenumber')
            house_number_tag.set('v', house_number)
            street_tag = ET.SubElement(node, 'tag')
            street_tag.set('k', 'addr:street')
            street_tag.set('v', street)
            city_tag = ET.SubElement(node, 'tag')
            city_tag.set('k', 'addr:city')
            city_tag.set('v', city)

    tree.write('formatted_addresses.osm')
if __name__ == '__main__':
    main()