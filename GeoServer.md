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
            - *Import vector layer* window will open, and  select the *shapefile* that n eed import in *PostgreSQL* along with that in the input section provide the table name and click on ok.![Import Vector layer](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/bhuwan/pictures/geoserver%20photo/import%20vector%20layer.png)
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
