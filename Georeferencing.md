**What is georefrencing?** \
Georeferencing is the process of transforming coordinate reference system(CRS) of raster data into the new real-world coordinates system. Coordinate system of the raster dataset that is to be georeferenced is known as source coordinate system(CRS) and CRS after georeferenced or output of georeferencing is known as destination CRS. Coordinates can be found in two different ways, one is that if there is mark in the map itself i.e. coordinates can be found in the map and the next is to have a field survey and point out the coordinated by the help of some identifiable things in the image or in the map. After having the ground control point(GCP), by the help of transformation functions raster data in source CRS is transformed to destination CRS. For the better transformation GCPs should be taken on the four corners of the image and some identifiable points in the middle of the image which may not be always possible but can result good transformation. For georeferencing, Geospatial Data Abstraction Library(GDAL) plugin is used which is a core QGIS plugin i.e. it will be already installed just need an activation.

**Why georeferencing?** \
We need to find out bin location as pointed in the map provided to us. We need to georeferenced the map so as to obtain coordinates of the bin so that we can use that coordinates to locate the bin in the real map as well as for the visualization.

**How to do georeferencing?** \
Raster image to be georeferenced: -

https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/sensor_node_ttn/Map_Moers.png

**Start Georeferencing: -**

 1. Launch *QGIS Desktop*
 2. GDAL Plugin installation or activation
	 - Navigate to *plugins* in QGIS
     - *Manage and install plugins*
	- Click on the *installed* tab
	- Find the *Georeferencer GDAL* and check the box
 3. Using OpenStreetMap as a base map for Ground Control Point(GCP)
	 - It is not necessary to use an openstreetmap as a base map. Maps like bing, google maps can be used
	 - To use this web based map services, open layer plugin need to be installed
	 - Same as other plugins, go to *plugins* menu and *manage and install plugins*
	 - Search open layer plugin and *install*
	 - It could be possible that it may not be there, it is because this plugin is an experimental plugin
	 - In that case enable “show also experimental plugin” from the *settings* tab
	 - Base map looks like as follow
	![basemap launch](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/georeferencing%20photo/basemap.png)

4. From *Raster* menu click *Georeferencer*, georeferencer window will opens
![Georeferencing window](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/georeferencing%20photo/georeferencing%20window.png)
	- Above shown is the georeferencing window
	- Upper part is Image window
	- Lower part is for Ground Control points(GCP) table

5. Load Raster image, clicking on *Open Raster* under *File*
6. Analysing both datasets for finding the precise location like corner of buildings or street intersection, locate the potential GCPs
	- From Image window of georeferencing window and QGIS base map
7. Zoom in to the specific area for GCP point in order to have precise value
	- Entering ground control points
		- Using the *add point tool*, enter first GCP into the georeferencer image window 
		- On the click on georeferencer image window, *Enter map coordinates window* will popups with the destination coordinates fields i.e X/East and Y/North boxes
		- On a click of *From map canvas* button you will be redirect to the QGIS where you can locate the same location and click there to populate the X and Y coordinates in the *Enter map coordinates window*	![map coordinates window](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/georeferencing%20photo/coordinate%20from%20canvas.png)
		- Now, GCP table in the Georeferencing window will be populated with source and destination coordinates of the first ground control point
		- Those GCP will be indicated by red dot on both georeferencing image as well as on QGIS Desktop map canvas 
			- In case of the point not being precise, the position of the control point can be changed by using *Move GCP Point tool* on both Georeferencer window or in QGIS Desktop map canvas 
			- Also, can be deleted with *Delete point tool*
		- First GCP point can be seen in figure below:
![1st gcp point](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/georeferencing%20photo/1st%20gcp%20value.png)
		- Repeat steps 2-6 for other GCP points, here 10 GCP points are taken
![10 gcp point](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/georeferencing%20photo/10%20sample%20gcp%20points.png)
		- Once the points are entered you can save GCP points as a text file of .points extension so that it can be reused, by clicking *Save GCP Points As*
8. Final Transformation to form Georeferenced image
		Before starting transformation steps, let's be clear about Transformation type, Resampling method fields, and other output settings.
     - Transformation type
     There are seven choices for transformation type which determines how the ground control points are used to transform the image from source to destination coordinate space. Each type has different results as explained below
	     - Linear: - 
		   Algorithm that creates a world file for the raster without actually transforming the raster. It can be used on images that are already in a projected coordinate reference system without having world file. Minimum two GCPs are required for the transformation.
	   - Helmert: -
	   Used form simple scaling and rotation, mainly used if the transformation simply involves a change from one projected CRS to another. Minimum two GCPs required for the transformation.
	   - Polynomial: -
	  It is of 3 types, Polynomial 1, Polynomial 2, Polynomial 3 which refers to the order of transformation i.e. Higher the transformation order the more complex distortion can be corrected with more computer power. Polynomial 1 requires 3 GCPs and used for stretched, scaled and rotated raster input. Polynomial 2 and 3 are used for bent or curved input with six and ten GCPs respectively.
	   - Thin Plate Spline: -
	   This algorithm introduces local deformations in the data. It is more modern georeferencing method and gives similar results as a higher-order polynomial transformation and more suitable for scanned images.
	   - Projective: -
	   This algorithm is useful for oblique images and some scanned maps. Better for Georeferencin satellite images such as Landsat and DigitalGlobe.
	   
	  - Resampling method: -
	  This setting is to determine how the pixel value will be calculated in the output raster. There are five different choices for resampling methods as follow
		  - Nearest neighbour: -
		Value of an output pixel is determined by the nearest cell in the input. This is fastest, suitable for categorical or integer data and will not change pixel value during transformation. Blocky output will be produced for continuous data.
		  - Linear: -
		  Produces smooth output as its output value is the weighted average of the four nearest input cell values. It removes the high and low input cell values and recommended for the continuous dataset.
		  - Cubic: -
		  Same as linear with 16 nearest input cell value and is better at preserving edges and generates sharper output than linear. Recommended for continuous data and widely used for aerial photography and satellite images.
		  - Cubic Spline: -
		Based on spline function and produces smooth output.
		  - Lanczos: -
		  Produces sharp value and should be careful because it can result both lower and higher output value then input value.
		  
	- Steps for transformation: -
		- After all the GCPs have been created, click on the *Transformation setting*
![Transformation setting](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/georeferencing%20photo/transformation%20setting.png)
		- Select appropriate transformation type and resampling type as per the requirement because there is no any best transformation type
			- Use Thin Plate Spline as it is more suitable for the scanned maps with fewer GCPs
		- Set the resampling method as required
			- Nearest neighbor is used for this tutorial
		- Check *Load in QGIS* when done to load the transformed map directly in QGIS
		- Residual [pixels] column in the GCP table will be populated, once the transformation setting values have been set which contains root mean square error(RMSE) for each GCP. This RMSE metric indicates the quality of transformation which depends on the transformation type chosen
		![Complete GCP table](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/georeferencing%20photo/after%20transformation.png)
		- By the general rule of thumb, RMSE should not be larger than half of the pixel size of raster in the map unit
		


   



