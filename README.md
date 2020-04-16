# Hawaii-Surfs-Up
<p align="center">
  <img width="800" height="500" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/surfs-up.png">
</p>

## Hawaii Precipitation And Temperature Observations
From this sqlite data retrieval of precipitation and temperature for various observation stations in Hawaii, we analyzed that months of August and April sees the maximum precipitation. 

<p align="center">
  <img width="800" height="500" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/Precipitation%20Graph.png">
</p>

This dataset also revealed that the most temperature observations have been seen the Station = ## WAIHEE 837.5, HI US with temperature ranging in 75-78 in the months of July, August, September and October respectively. 

<p align="center">
  <img width="800" height="500" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/Station%20Temperature%20Observations.png">
</p>

## Flask API
Creating the API endpoints to retrieve the rainfall and temperature data(s). 

        "/api/v1.0/precipitation<br/>" - Displays the precipitation data for one year
        "/api/v1.0/stations<br>" - Displays all the stations observed for this dataset
        "/api/v1.0/tobs<br>" - Temperature observations made over one year. 
        "/api/v1.0/<start><br>" - Displays the temperature min, max and avg for the specified date.
        "/api/v1.0/<start>/<end><br>" - Displays the temperature min, ,max, avg for specified date range. 
