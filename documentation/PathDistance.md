# Georeferencing and calculating minimum distance and shortest path

## Introduction
Given the image file of Moers city and coordinate points of the locations of the garbage bins, the main task was to do georeferencing and finding the shortest path as well as shortest distance from a particular bin to any other bins. In this task, GQIS 2.18 and 3.0 versions were used and different methodologies were followed to calculate the desired results. 

## Tools and methodologies:

### QGIS: 
QGIS is a C++ written open source desktop platform which supports vector layers, raster layers and works with geospatial data and analyzes them. QGIS is also used for georeferencing and measuring distance between two points and finding the best route and shortest time to reach it. To measure the minimum distance of two individual locations, QGIS 3.0 was used and to get the shortest route and time, QGIS 2.18 was used.

### Distance Matrix: 
Distance matrix is a table which shows the distance from a particular point to another point. In QGIS, to find which point is near to a specific point, distance matrix is used. After plotting, georeferencing all the points and getting the shapefile of Moers map, distance matrix was used to find the minimum distance. Under the vector analysis tools, the distance matrix is there for the distance analysis.

### Shortest path: 
Another feature which was done in this task was finding the shortest path using Dijkstra shortest path algorithm. For this, Road Graph plugins were installed in QGIS. With the Moers map shape file and Moers map OSM file, the shortest path tool was run to calculate the shortest path and time to reach from a bin to another bin.

## Results:
Using distance matrix to find minimum distance and shortest path algorithm to find shortest path and time were done successfully. With the help of distance matrix, it is easy to find the nearest point to a coordinate. With the help of distance matrix, it was able to find the minimum distance from a specific bin to other bins and which bin is the closest bin in terms of distance. But measuring the shortest distance should not be primary criteria while it can be possible that there is traffic signal or much time to reach the bin which has the minimum distance from a bin. For this complexity, a solution was to find the shortest path and time to reach a bin using shortest path algorithm. 


![Image description](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/ashikul/Screenshot%20(15).png)
            Figure 1: minimum distance from a coordinate point to other points

![Image description](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/ashikul/Screenshot%20(17).png)
            Figure 2: finding shortest path and time using shortest path algorithm
