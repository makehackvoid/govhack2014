## Preface
In this document we will cover the initial setup of a basic environment required to fix minor issues with the upstream data from act art

## Prerequisites
- Internet connection
- Debian Wheezy (process can be ported by the the commands are based on Wheezy)
- [Canberra Suburb Boundaries](http://data.gov.au/dataset/canberra-suburb-boundaries)

## Preparing the environment

1) Perform the following
> apt-get install postgresql-9.1-postgis

> su postgis

> createdb "postgis_template"

> cd /usr/share/postgresql/9.1/contrib/postgis-1.5

> psql -d postgis_template -f postgis.sql

> psql -d postgis_template -f spartial_ref_sys.sql

> createdb -T postgis_template act_shape

2) nano /etc/postgresql/9.1/main/pg_hba.conf
Locate line which has: 
> local    all    postgres    user

And change it to

> local    all    postgres    trust

3) Setup additional dependancies (NB: These dependencies can be setup inside of a python virtual environment)
> apt-get install postgresql-server-dev-9.1

> pip install psycopg2

## Populating the database
> su postgres

> mkdir /act_shape

> mkdir /act_shape/fixed

> cd /act_shape

> unzip ~/Downloads/*ACT_Administration_Boundaries.zip

> ogr2ogr -f "ESRI Shapefile" /act_shape/fixed/ACT_DIVI_WGS84.shp /act_shape/ACT_DIVI.shp -t_srs EPSG:4326

> shp2pgsql /act_shape/fixed/ACT_DIVI_WGS84.shp | psql -U postgres act_shape

Use the following command to verify that the coords are in decimal degrees

> psql -U postgres act_shape -c "SELECT ST_AsText(the_geom) FROM act_divi_wgs84"
