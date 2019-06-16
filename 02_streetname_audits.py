#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
from collections import defaultdict
import xml.etree.cElementTree as ET
import pprint
import re
import datetime
print(datetime.datetime.now())
osm_file = open('ohio-latest.osm','r')
#13,5
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
street_types = defaultdict(set)

expected = ["Street","Avenue","Boulevard","Drive","Court","Place"]

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:sttreet")

def audit():
    for event, elem in  ET.iterparse(osm_file,events=("start",)):
        if elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    pprint.pprint("Checking " + tag.attrib['v']) 
                    audit_street_type(street_types, tag.attrib['v'])
    pprint.pprint(dict(street_types))
    print(datetime.datetime.now())
    return

if __name__ == '__main__':
    audit()




def count_tags(filename):
    tags = defaultdict(int)
    for event, elem in  ET.iterparse(filename):
        tags[elem.tag] += 1
    return tags
            



def test():

    tags = count_tags('ohio-latest.osm')
    pprint.pprint(tags)
    #assert tags == {'bounds': 1,
     #                'member': 3,
      #               'node': 20,
       #              'osm': 1,
        #             'relation': 1,
         #            'tag': 7,
          #           'way': 1}

    

if __name__ == "__main__":
    test()