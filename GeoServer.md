**Geoserver**

Geoserver, open source software server written in Java which allows us to edit, process and share geospatial data. It is designed for interoperability and publishes data from any major spatial data source using open standards. It is an Open Geospatial Consortium(OGC) compliant implimentation of a various open standard such as Web Feature Service(WFS), Web Map Service(WMS), and Web Coverage Service(WCS).
In this project, we are using this Geoserver to visualize the bins that are located in different places and also indicate the status of bin. For performing visualization, we need to have spatial data in the database, access to the database, QGIS, and ofcourse  Geoserver installed in our processor.

 1.  Geoserver Installation 
		- *Follows the link* for the [Installation of GeoServer](https://docs.geoserver.org/stable/en/user/installation/index.html#installation)
 2.  Start Visualization using GeoServer 
		-  Launch GeoServer 
		- For starting server, 
		  - *Click* on Server ->Start
		 - In a web browser, *navigate* to http://Localhost:8080/geoserver
			 - Admin as username
			 - Password: geoserver
![Loginpage of GeoServer](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/geoserver%20login%20page.png)
          - After login, Administrative function is accessible as shown below
![AdministrativeFuntion](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/geoserver%20after%20lonin.png)
           - For the seperate work around, *create* a Workspace
