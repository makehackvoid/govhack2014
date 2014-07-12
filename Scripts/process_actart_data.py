#!/usr/bin/python

# DEPENDANCIES
# pip: psycopg2,urllib2,json
# apt: postgresql-server-dev-9.1

import psycopg2
import json
import urllib2

# CONFIG
targeturl = 'http://www.data.act.gov.au/resource/j746-krni.json'
connection_string = 'dbname=abs_sa1 user=postgres'
outputfile = 'output.json'

print('Retrieving JSON')
opener = urllib2.build_opener()
f = opener.open(targeturl)
jres = json.load(f)

newdict = []

for item in jres:
    # THIS CODE HERE ACTUALLY IS TO BE IN A LOOP!
    lat = item['location']['latitude']
    lon = item['location']['longitude']
    coord = lon + ' ' + lat

    blank = False

    if blank is False:
        print 'Searching database for ', coord
        # coord = '149.234167 -35.353333'
        sql = "SELECT * FROM sa1_2011_aust WHERE ST_Intersects(ST_GeomFromText('POINT("+coord+")'),the_geom) LIMIT 10;"
        # ^---- We have to concat here because if we pass it via parameters it will automatically enclose in single quotes
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()
        res = cur.execute(sql)
        rows = cur.fetchall()
        conn.close()

        item['local_region'] = item['suburb']

        if len(rows) == 1:
            item['suburb'] = rows[0][5]
        else:
            item['suburb'] = ''

        newdict.append(item)

f = open(outputfile, 'w')
f.write(json.dumps(newdict))
f.close()
