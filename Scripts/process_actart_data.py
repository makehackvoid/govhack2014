#!/usr/bin/python

# ################################
# DEPENDANCIES
# python ver: 3.4
# pip: psycopg2,urllib2,json
# apt: postgresql-server-dev-9.1
# ################################

import psycopg2
import json
import urllib.request as ur_req

# ##########################
# CONFIG
# ##########################
targeturl = 'http://www.data.act.gov.au/resource/j746-krni.json'
tablename = 'act_divi_wgs84'
database = 'act_shape'
connection_string = 'dbname='+database+' user=postgres'
outputfile = 'output.json'

# CONFIG - Column Index Definitions
suburbNameColIndex = 3  # Required
divCodeColIndex = 2  # Optional - set to None to disable
diviColIndex = 4  # Optional - set to None to disable

# ###########################################
# NO USER SERVICABLE PARTS BEYOND THIS POINT
# ###########################################

print('Retrieving JSON')

resp = ur_req.urlopen(targeturl)
jres = json.loads(resp.readall().decode('utf-8'))

newdict = []

for item in jres:
    lat = item['location']['latitude']
    lon = item['location']['longitude']
    coord = lon + ' ' + lat

    print('Searching database for ', coord)

    sql = ("SELECT * FROM "+tablename+" " +
           " WHERE ST_Intersects(ST_GeomFromText('POINT("+coord+")'),the_geom) LIMIT 10;")
    # ^---- We have to concat here because if we pass it via parameters it
    # will automatically enclose in single quotes
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    res = cur.execute(sql)
    rows = cur.fetchall()
    conn.close()

    item['local_region'] = item['suburb']

    if len(rows) == 1:
        item['suburb'] = rows[0][suburbNameColIndex]
        if divCodeColIndex is not None:
            item['div_code'] = rows[0][divCodeColIndex]
        if diviColIndex is not None:
            item['divi'] = rows[0][diviColIndex]
    else:
        item['suburb'] = ''
        if divCodeColIndex is not None:
            item['div_code'] = ''
        if diviColIndex is not None:
            item['divi'] = ''

    newdict.append(item)

f = open(outputfile, 'w')
f.write(json.dumps(newdict))
f.close()
