To parse the ACT_DIVI dataset available at http://data.gov.au/dataset/canberra-suburb-boundaries

1. Install GDAL: `brew install gdal`
2. Install Topojson: `npm install -g topojson`
3. Run the following command:
    `rm -f suburbs.json | ogr2ogr -f GeoJSON -where "DIVI NOT IN ('THAR', 'OAKS', 'BEAR', 'HUME', 'HALL', 'PIAL')" suburbs.json ACT_DIVI.shp -t_srs EPSG:4326 | topojson -p name=DIVISION,id=DIVI --id-property DIVI -o suburbs.topo.json suburbs.json`
