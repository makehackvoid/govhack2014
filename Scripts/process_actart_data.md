doco so far (just putting it here as somewhere quick and dirty

* Fire up a Debian Wheezy system (some packages may be translatable to other operating systems. ymmv)
* Install postgis -> apt-get install postgresql-9.1-postgis
* su postgres
* fire up psql CREATE DATABASE postgis_template; CTRL + D (disconnect)
* cd /usr/share/postgresql/9.1/contrib/postgis-1.5
* psql -d postgis_template -f postgis.sql
* psql -d postgis_template -f spartial_ref_sys.sql
* createdb -T postgis_template abs_sa1

* disable authentication on postgresql (this process is a one off)

* CHANGE in /etc/postgresql something/pg_hba.conf
* local all postgres user
* to 
* local all postgres trust

* sudo apt-get install postgresql-server-dev-9.1
* sudo pip install psycopg2