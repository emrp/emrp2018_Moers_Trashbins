What is Georeferencing in QGIS ? 


Georeferencing is process of providing real world coordinates and values to each and every pixel in raster data. Georeferencing is mainly used in collecting the longitude and latitude coordinates of the raster data. We have to give the fixed location and by the help of  georeferencing we can get the fixed latitude and longitude value of the desired location. It is mainly used in field map survery where we need GPS value of certain location. While doing georeferencing a special care should be taken while selecting points in the map so that we can achieve high accuracy in georeferencing and produce a high accurate map with accurate coordinates. 

Overview of the project:: In this project we are doing the georeferencing in certain image. We have map of city moers in which there is pictures of the bin located in the image. We have to find the exact longitude and latitude value of bins in the image. In the image we can see the yellow dots representing the bins in the image. Our task is to find exact longitude and latitude of those bins which are present in the map. For that purpose we need georeferencing. 





We will use the map of moers for this project. This map has been provided to us by Moers city center department’s people. 

Steps for georeferencing

1. First thing first for using the georeferencing we need to install the “Georeferencer GDAL” plugin. This is a core plugin, which is already installed in your QGIS you just need to enable this plugin in order to use it. To enable this plugin go to Plugins>Manage and Install plugins. You will see the list of the plugins in ALL section then search for georeferencer GDAL plugin. Tick mark that plugin and this will enable the plugin.




2. The georeferencer plugin is installed in the Raster Menu. Click on the Raster>Georeferencer to open the plugin.












3. After clicking the georeferencer plugin, anohter window will add up. This the georeferencer window. This window consist of two sections: top section where raster will be displayed and bottom section where  Ground Control Points (GCP) will be shown.



4.  Now to open our image file. Go to the Files>Open Raster. Browse and select the image that we need to find the location of.













5.  After that you will see map being loaded in the raster section of georeferencer.  In my case I have uploaed map of moers and that map is being shown in the raster section. 





6. Now its time to do some setting changes. In the georeferencer click on Transformation Settings. You will see another box.

Make sure you choose these settings before beginning your process: 

Transformation type : Thin Plate Spline
Resampling method : Nearest neighbour
Target SRS : EPSG 4647

In the Output raster, browse and selec where you want to show your output raster file. 

































7. You can either Zoom in or zoom out and control the map with options that are being provided in the georeferencer tool bar.











8.  Now our task is to assign the coordinates of the bin in the map. For this click on Edit>Add Point in the toolbar and click on one of the bin location in the map.  You will see the cursor sign in being changed. Lets Suppose I click on the orange point which is near to number 3. 






9. Another window will pop up asking about the Enter Map Coordinates. You can see From map canvas option below. Click on that option.






10.  After clicking From map canvas option, you will be redirected to the QGIS main page whete you need to first intall the OpenLayer plugin.  For that go to plugins>Manage and install plugin there you can at first install the OpenLayer plugin. After installing the plugin you can find that installed plugin in Web>OpenLayers plugin.

To open the map, go to the Web>OpenLayers plugin>OpenStreetMap. After this you can see a world map being loaded in the raster of QGIS. Zoom into the Germany and Moers city as we are dealing with the map of moers in this project. You can use Zoom in option and find Moers which is located at the West Germany. 

After that you can match the image file we have with the map of moers in the QGIS. And we have already selected a point in the georeferencer and try to find the same exact location in the map so that we could get the accurate point and accurate latitutde and longitude values. 







11. After clicking on the accurate location we will get the coordinates of that point and that points will be reflected in the georeferencer. The Enter Map Coordinates will show the coordinates of the points that we have just clicked. Click on OK. 



















12.  You can find that GCP table now will have a row with details about location.






13.  Similarly, add more locations from the map with the similar process. More the number of points, more the accurate image and results. In the figure below you can see number of points being taken and it will be added in the list. 




14.  Go to the File>Start Georeferencing to get our things started.
















15. Once georeferencing has been completed you can see georeferenced layer in the QGIS.



















16.  Finally after taking number of points we finally complete out georeferecing part. Always zoon in to take the point and choose the points in the building as they are easy to locate in the actual map and take many points to get the accurate result. Always make sure that the EPSG remains same for all. In this I have take EPSG 4647. 
