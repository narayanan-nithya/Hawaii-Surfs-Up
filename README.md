# Hawaii-Surfs-Up
<p align="center">
  <img width="800" height="500" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/surfs-up.png">
</p>

## Hawaii Precipitation And Temperature Observations
From this sqlite data retrieval of precipitation and temperature for various observation stations in Hawaii, we analyzed that months of August and April sees the maximum precipitation. 

<p align="center">
  <img width="300" height="300" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/Precipitation%20Graph.png">
</p>

This dataset also revealed that the most temperature observations have been seen the Station = ## WAIHEE 837.5, HI US with temperature ranging in 75-78 in the months of July, August, September and October respectively. 

<p align="center">
  <img width="300" height="300" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/Station%20Temperature%20Observations.png">
</p>

## Flask API
Creating the API endpoints to retrieve the rainfall and temperature data(s). 

<p align="center">
  <img width="200" height="200" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/D20486DA-8180-4136-A4A6-01344201C65C_4_5005_c.jpeg">
</p>
        "/api/v1.0/precipitation<br/>" - Displays the precipitation data for one year
<p align="center">
  <img width="300" height="300" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/102099D5-BA36-4940-A853-BBDE60C720A5_4_5005_c.jpeg">
</p>
        "/api/v1.0/stations<br>" - Displays all the stations observed for this dataset
<p align="center">
  <img width="300" height="300" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/102099D5-BA36-4940-A853-BBDE60C720A5_4_5005_c.jpeg">
</p>
        "/api/v1.0/tobs<br>" - Temperature observations made over one year. 
<p align="center">
  <img width="300" height="300" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/03CB4CC6-CBB5-4EA8-86F0-432DFFE68F6B.jpeg">
</p>
        "/api/v1.0/<start><br>" - Displays the temperature min, max and avg for the specified date.
<p align="center">
  <img width="300" height="300" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/1A98D96B-2321-43BC-B9DA-0E3B15003FDB.jpeg">
</p>
        "/api/v1.0/<start>/<end><br>" - Displays the temperature min, ,max, avg for specified date range. 
<p align="center">
  <img width="300" height="300" src="https://github.com/narayanan-nithya/Hawaii-Surfs-Up/blob/master/40D9A542-539D-4666-9122-9B573B8E3492.jpeg">
</p>
