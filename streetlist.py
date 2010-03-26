#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('edinburgh-highways.osm')
waylist =xmldoc.getElementsByTagName('way')

ways = {}

for ways in xmldoc.getElementsByTagName('way'):
  tag = {}
  name = ""
  highway = ""
  ref_name = ""
  surface = ""
  for tag in ways.getElementsByTagName('tag'):
    k = tag.attributes['k']
    v = tag.attributes['v']
    if k.value == 'name':  name = v.value
    if k.value == 'highway':  highway = v.value
    if k.value == 'ref': ref_name = v.value
    if k.value == 'surface': surface = v.value
  print "%s,%s,%s,%s" % (highway, name, ref_name, surface)
