#! /usr/bin/python

import csv

osmStreetReader = csv.reader(open('osm_streets.txt'), delimiter=',')

# Build a dictionary lookup based on either the name (row[1]) or the ref (row[2])

d = {}

for row in osmStreetReader:
#  print ','.join(row)
  if row[1] : 
    d[row[1]] = ','.join(row)
  elif row[2] :
    d[row[2]] = ','.join(row)

# Open the roads file and try and find these in the edinburgh list

file= open( "roads.csv", "rU")
for streetRow in file: 
  streetRow = streetRow.replace('\n', '')
  list = streetRow.split('\t')
  street =  list[0].replace('"', '')
  try:
    print "%s,%s" % ( d[street], ','.join(list) )
  except KeyError: 
    print  ",,,,%s"  % ( ','.join(list) )
file.close()




