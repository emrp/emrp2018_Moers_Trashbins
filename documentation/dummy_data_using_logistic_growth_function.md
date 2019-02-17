# Uploading dummy data to database using logistic growth function  
The tool for python programming is Jupyter Notebook  
## Following Python Libraries are being used  

* numpy   
* matplotlib  
* psycopg2  
## The procedure to install the libraries is give below  
Before installing any library make sure that path for pip is defined in Environment Variable  
pip install numpy  
pip install matplotlib  
pip install psycopg2 
for working with Jupyter Notebook the installation is through Anaconda prompt  
conda install psycopg2  
or you can upgrade your pip if the is problem in installation
python -m  pip install --upgrade pip
## After installing the above mentioned libraries  
The script contain a class DatabaseConnection with   
* constructor  
and a function  
* insertTTNGateway  
## The Core  
The idea is to measure the level of garbage after 15 minutes  
The bin carrying capacity level is 100  
The growth rate for accumulation of garbage is set to 0.25
## The Result  
![latest](https://user-images.githubusercontent.com/26201860/52905526-b99c5380-323b-11e9-833f-e9ecfe00ffe5.PNG)
