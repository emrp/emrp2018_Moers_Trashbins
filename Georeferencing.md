**What is georefrencing?**

Georeferencing is the process of transforming coordinate reference system(CRS) of raster data into the new real-world coordinates system. Coordinate system of the raster dataset that is to be georeferenced is known as source coordinate system(CRS) and CRS after georeferenced or output of georeferencing is known as destination CRS. Coordinates can be found in two different ways, one is that if there is mark in the map itself i.e. coordinates can be found in the map and the next is to have a field survey and point out the coordinated by the help of some identifiable things in the image or in the map. After having the ground control point(GCP), by the help of transformation functions raster data in source CRS is transformed to destination CRS. For the better transformation GCPs should be taken on the four corners of the image and some identifiable points in the middle of the image which may not be always possible but can result good transformation. For georeferencing, Geospatial Data Abstraction Library(GDAL) plugin is used which is a core QGIS plugin i.e. it will be already installed just need an activation.


**Why georeferencing?**
We need to find out bin location as pointed in the map provided to us. We need to georeferenced the map so as to obtain coordinates of the bin so that we can use that coordinates to locate the bin in the real map as well as for the visualization.

**How to do georeferencing?**
Raster image to be georeferenced: -

https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/sensor_node_ttn/Map_Moers.png

**Start Georeferencing: -**

 1. Launch *QGIS Desktop*
 2. GDAL Plugin installation or activation
         - Navigate to *plugins* in QGIS
         - *Manage and install plugins….*
         - Click on the *installed* tab
         - Find the *Georeferencer GDAL* and check the box
 3. Using OpenStreetMap as a base map for Ground Control Point(GCP)
	 - It is not necessary to use an openstreetmap as a base map. Maps like bing, google maps can be used
	 - To use this web based map services, open layer plugin need to be installed
	 - Same as other plugins, go to *plugins* menu and *manage and install plugins…*
	 - Search open layer plugin and *install*
	 - It could be possible that it may not be there, it is because this plugin is an experimental plugin
	 - In that case enable “show also experimental plugin” from the *settings* tab


   



