To parse the SSC_2011_AUST dataset available at http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055003_ssc_2011_aust_shape.zip&1270.0.55.003&Data%20Cubes&D68DFFC14D31F4E1CA2578D40013268D&0&July%202011&22.07.2011&Previous

1. Rename all SSC_2011_AUST.* files to suburbs.*
2. Install GDAL: brew install gdal
3. Install Topojson: npm install -g topojson
4. Run the following command:
    rm -f suburbs.json | ogr2ogr -f GeoJSON -where "SSC_CODE LIKE '8%' AND SSC_CODE <> '80094' AND SSC_CODE <> '80085' AND SSC_CODE <> '80078' AND SSC_CODE <> '80048'" suburbs.json suburbs.shp | topojson -p name=SSC_NAME --id-property SSC_CODE -o suburbs.topo.json suburbs.json
