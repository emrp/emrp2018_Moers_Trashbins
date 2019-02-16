
**Geoserver**

Geoserver, open source software server written in Java which allows us to edit, process and share geospatial data. It is designed for interoperability and publishes data from any major spatial data source using open standards. It is an Open Geospatial Consortium(OGC) compliant implimentation of a various open standard such as Web Feature Service(WFS), Web Map Service(WMS), and Web Coverage Service(WCS).
In this project, we are using this Geoserver to visualize the bins that are located in different places and also indicate the status of bin. For performing visualization, we need to have spatial data in the database. For the spatial data, QGIS will be need for the extracting shape file and store that data in the PostgreSQL Database and  then proceed with Geoserver installed in our processor.

 1. Adding *Geospatial data* in the *PostgreSQL database* using *QGIS*
      - Establishment of connection, *QGIS* with *PostgreSQL*
        - Launch *QGIS*
         - Add the *shapefile* in *QGIS* that needs to be stored in *PostgreSQL*
          	- Layer->Add layer->Add raster layer
         - Add PostGIS layer
         	- Layer->Add layer->Add PostgreSQL layers![Data Source Manager](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/Screen%20Shot%202019-02-12%20at%208.39.28%20PM.png)
        - *Data Source Manager* | *PostgreSQL* window will open,  add connection to the *PostgreSQL*
	         - Click on *New* then that will prompt *create a New PostgreSQL Connection window*  
	         - And then provide connection information like *Name, Host, Port, Database and SSL mode*![Create a New PostgreSQL Connection](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/Screen%20Shot%202019-02-12%20at%208.43.40%20PM.png)
	         - Enter the credential of *PostgreSQL* database![Enter Credential](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/Screen%20Shot%202019-02-12%20at%208.44.03%20PM.png)
	         - After that *Connection Successful* message will popup
	        
        - Transfering data from *QGIS* to *PostgresSQL*
            - Open *DB Manager* in *QGIS*
              - Locate *Database->DB Manager*
            - On the right panel, locate *PostgreSQL* and expand it 
            - Then there will be availbility of database that connected previously![PostgresSQL database availibility](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/Screen%20Shot%202019-02-12%20at%208.52.32%20PM.png)
            - After that need to provide *credential*  to access the database and connected database display as belows![Database connection](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/Screen%20Shot%202019-02-12%20at%208.58.28%20PM.png)
            - Click on *Import layer/File*
            - *Import vector layer* window will open, and  select the *shapefile* that need import in *PostgreSQL* along with that in the input section provide the table name and click on ok.![Import Vector layer](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/import%20vector%20layer.png)
            - Now the shape locate in *PostgreSQL* and  previews as below![Shape file import in PostgreSQL](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/shapefile%20imported%20in%20postGIS.png)
            
        
 2.  Geoserver Installation 
		- Follows the link for the [Installation of GeoServer](https://docs.geoserver.org/stable/en/user/installation/index.html#installation)
 3.  Start Visualization using GeoServer 
		-  Launch *GeoServer* 
		- For starting server, 
		  - Click on *Server ->Start*
		- In a web browser, navigate to *http://Localhost:8080/geoserver* 
		- Provide the following credential for default configuration
			 - *Admin as username*
			 - *Password: geoserver*
![Loginpage of GeoServer](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/geoserver%20login%20page.png)
         - After login, *Administrative functions* is accessible as shown below
![AdministrativeFuntion](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/geoserver%20after%20lonin.png)
          - For the seperate work around, create a  new Workspace
			 - Navigate *Data on right panel* and click on *Workspace*![Workspace panel](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/workspace.png)
			 - And then click on a *Add new workspace* 
			 - Provide Name as an identifier for a any project![New Workspace Outline](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/new%20workspace.png)
				 +  "*Where Name Not more than 10 characters and exclude blank space with that, and -   Namespace Uniform Resource Identifier(URI) can usually be any URI that is not necessary to resolve to an actual valid web address so we can give any URI that associate our project*"
			 - Click on *submit*, and then new workspace will be added in the list of Workspace
			 
			 
 4. Creating Store for the integration of data
	 - Navigate to *Data->Stores*
	 - Click on *add new store*
	 - In the Vector Data Source, there will be  *PostgreSQL – PostgreSQL Database*, click on it![Vector Data Source](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/New%20store.png)
	 - Complete *Basic Store* Info
		 - Select a *Workspace* that  created  previously
		 - Provide the data source name
	- Configure following  all the *Connection Parameter* for *PostgreSQL connection*![Connection parameter](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/connection%20parameter.png)
	- All other *fields* can be left as it is and  Save the *store*
	- And then *New Layer* tab will open
	- After that select the *table* having *shapefile* and press on *publish*
	- In the edit layer, provide *Name*, *Title* and *Abstract*![Edit layer](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/edit%20layer%20detail.png)
	- Generate the layer’s *bounding boxes* by clicking the *Compute from data* and then *Compute from native bounds links*![Boundaries box](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/Bounding%20Boxes.png)
	- Click *Publishing* tab for *style selection* and for the case of style for now *default* can selected and then this layer will be available in the *Layer* and *Layer preview*
	- To view the *preview* navigate *Data->Layer preview*
	- Click on the newly created layer, in this case Location_shapefile, it looks like this![Layer of shape file](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/layer%20of%20shapefile.png)
 5.  Adding *web maping service (WMS)* as base map to see the above shape fiel location in map
	 - Navigate *Data->Stores->Add New Store*
	 - From *Other Data Sources* select *WMS – Cascade a remote web map service*
		 - There are many web map servers, here we use web map service from Mundialis, because it is free and based on open access data also comply web map service specification of OGC
		 - Copy the service URL provided  -   [https://www.mundialis.de/en/ows-mundialis/](https://www.mundialis.de/en/ows-mundialis/)
		 - Enter the basic info providing *WMS* source name and description also workspace along with connection information as belows![Connection information](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/connection%20info.png)
			 - Paste the service URL in the *Capabilities URL* and leave other *default value*
		 - New Layer addition tab will open and Select *TOPO-OSM-WMS* and click *publish*
		 - This layer will be added in the *layer list* and  preview to see how it looks![Layer list for newly added layer](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/layer%20list.png)
 6. Combining two layers, *shape file layer* and *WMS* layer \
In order to have the shapefile above the base map and to see the location of bins in the map we need to combine the layers
	 - Navigate  *Data>Layer Groups*
	 - Click on *Add new layer group*
	 - Provide *Name*, *Title* and *Workspace* in the layer group as belows![Layer group](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/add%20layer%20group%20field.png)
	 - In  the *layer section*, click on *Add Layer*
		 - Select base map, as *TOPO-OSM_WMS_emrp_project*, *It should be selected first* 
		 - Select Location *shapefile*![Layer group ](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/adding%20layer.png)
			 - *Base map to select first because shapefile should be above the base map layer else shape points will be hidden by the base map*
		  - Click on *Generate Bounds* to generate coordinate in the Bounds box![Boudaries for two layer](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/added%20layer%20bound%20value.png)
		  - Save the *layer*, *New layer group* will be listed in the list of layer groups
		  - Click on *layer preview* and select the *layer* just create which looks like this![layer combine map](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/layer%20combine%20map.png)
 7. Styling \
Data is visualized in Geoserver. Now to  play with the style for the appearance of geospatial data. There are different formats for styling
	 - *Styled Layer Descriptor(SLD)*: *Default styling* for geospatial styling and *OGC standard*
	 - *Cascading Style Sheet(CSS): CSS- syntax*
	 - *YSLD*: *SLD-equivalent based on YAML* for improved authority
	 - *MBStyle*: A syntax based on *JSON* for improved interoperability
Now to show the unique ID of the BIN and its location styling been used.
	- Click on *Data->styles*
	- Click on *Add new style* for creating our own style
	- Provide the *Name* and *Workspace*![Style page](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/style%20page.png)
		- *SLD* format is used for this project and selected *default style* and start editing those in our own way for simplicity
	- Selected the  *point* and click on *generate*
	- Then *XML code* will appear in the *Style Editor*![Style editor](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/style%20editor.png)
		- We are trying to show the attribute like *Bin_ID* so we need to add our own rule to display the attribute value that we have from the *PostgreSQL database*
	- Adding rule for display of *Bin_ID*![Style ID](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/style%20for%20id.png)
		- Created own rule where *Text Symbolizer* for Displaying text i.e. ID of Bin
		- Label for displaying as a label for each point
			- Label contains
				- Name of *attribute* i.e. name of Bin 
				- Latitude
				- Longitude
		- Anchor point sets the point of intersection between *label* and *point* 
		- Displacement sets the offset of the label relative to the line, here 0 pixel horizontally and 5 pixels vertically
		- Vendor Option function defines that label overlaps or no
			- Positive value blocks overlapping
			- Negative value shows all the labels even they overlap
	- Also, able to  play with *point symbolizer* changing its shape and color also can use image if required
	- *Validate* needed before saving
	- click on *submit* for completion
 8. Applying User define style in the Visualization
	 - Click on *Data->Layer*
	 - Select the Layer that been created  the shapefile, here *Location_shapefile*
	 - Click on *Publishing* and select  style that been created previously![Point style](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/sty;e%20selection.png)
	 - Click on *Save*
	 - Click on *layer preview* and select  *layer to display*
	 - Click on Open layer of visualization_bin ![Labelling](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/labeling.png)
 9. Visualization with label status could look like![Labelling](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/status.png)
	 - Blue shows not need to serviced
	 - Red shows bin are full need to serviced 
