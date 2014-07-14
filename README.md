ACTifacts: ACT Public Art
===========
[![Build Status](https://travis-ci.org/makehackvoid/govhack2014.svg?branch=master)](https://travis-ci.org/makehackvoid/govhack2014)

##Summary

ARTifacts uses data from the ACT Public Art List to provide Canberrans and visitors to the ACT with information about the ACT's vibrant selection of public art. It is designed primarily as an ambient display of local art for display screens dotted around Canberra and surrounds.

The data is delivered as a web app, with the potential for the display to be customised for screens in different locations so that the entries displayed are weighted towards nearby art works. The focus is on a simple, elegant view of the artifacts together with information about where they are.

*  GovHack 2014 project page: http://hackerspace.govhack.org/content/artifacts-act-public-art
*  Demo version of ARTifacts: http://govhack.makehackvoid.com/

##Dataset challenges

The ACT Public Art List data set includes a field labelled 'suburb', but which actually contains districts (i.e. 'Gungahlin' rather than 'Ngunnawal'). To enable users to search for art in or near a specific suburb rather than the broader district, we have merged in ACT suburb shapefile data and correlated the GPS coordinate data in the ACT Public Art List data set with the suburb in which they are located. This data could easily be incorporated into the ACT Public Art List data set to improve its usefulness for other potential users in future.

We have documented the process for populating a database with shape file data on the project github wiki at https://github.com/makehackvoid/govhack2014/wiki/How-to-setup-the-data-i...

In addition, we found that many of the image URLs in the data set were no longer valid, meaning that we couldn't rely on them to be incorporated automatically when displaying the images from the artsACT website. To work around this issue, we created a web-scraper to scrape the ACT Public Art Database website to retrieve the correct current URL for each image. We would like to see artsACT implement an automated process of updating the ACT Public Art List regularly—the web-scraper we created for this project has been open-sourced as part of GovHack, and artsACT is of course welcome to use it to assist with keeping the database up-to-date if they find it useful. :-)

We have documented the process for populating a database with updated image URLs on the project github wiki at https://github.com/makehackvoid/govhack2014/wiki/Get-the-updated-photos

##Future enhancements

For the ambient display, we would like to add information about the distance and direction of nearby art works based on the location of the screen. We are also looking at adding road information to the map and suburb names to zoomed in map to make the location easier to recognise.

We intend to extend the web app to support an interactive mode where a user can optionally search for works based on criteria contained in the data set and data merged in from other sources. The user will be able to search by work title, artist, medium, and suburb. Additionally, the user will be able to set their location so that they can be shown art works within a specified distance from them. If the user is accessing the app via a location-aware device (smartphone, tablet, etc.), they will have the option to share their device's GPS location info with the app to set their location automagically.

As part of the project we were working on incorporating mapping and roads data from OpenStreetMap. Due to time constraints this is not included in the demo version, but will be completed as part of our post-GovHack tidy-up.

##Datasets Used

ACT Public Art list - https://www.data.act.gov.au/Education/ACT-Public-Art-List/j746-krni [artsACT] Canberra Suburb Boundaries - http://data.gov.au/dataset/canberra-suburb-boundaries [Office of the Surveyor-General, Environment and Sustainable Development Directorate] OpenStreetMap data - http://www.openstreetmap.org/ [ACT data set extracted using http://download.bbbike.org/osm/]

Contributing
------------
See `CONTRIBUTING.md`

Team
----
Name    | Username
------- | ------------------------------------------
Adam    | [voltagex](//github.com/voltagex)
Al      | [taxles](//github.com/taxles)
Brenda  | [brendam](//github.com/brendam)
Calum   | [talsidor](//github.com/talsidor)
Cameron | [cmrn](//github.com/cmrn)
Jamie   | [jamiereid](//github.com/jamiereid)
Jessica | [itgrrl](//github.com/itgrrl)
Max     | [mbainrot](//github.com/mbainrot)
Megan   | [prototypdino](//github.com/prototypedino)
Zak     | [balfourianae](//github.com/balfourianae)
