<div align="center">
  <img src="https://media.npr.org/assets/img/2017/04/25/istock-115796521-fcf434f36d3d0865301cdcb9c996cfd80578ca99-s1300-c85.jpg"><br>
</div>

# Description
We design this web applications to collect track paths of squirrels near the Central Park in NYC. We import `the 2018 Central Park Squirrel Census data`_ and allow our users to add, update data and view squirrel-sightings map. The link to the original database is: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/ We choose the attributes that we find interesting to put into our databases.



# Management Comand
- import squarrel data to django database
  - $ python manage.py import_squirrel_data /path/to/file.csv
- export database in django to local 
  - $ python manage.py export_squirrel_data /path/to/file.csv
 
# Website Functions
- view the details of each squirrel sighting on home page
- update the details of each squirrel sighting
- add a new squirrel sighting to database
- view the location of 100 squirrel sightings in central park on the map 
- get a general view of squirrel sightings statistics (counts of running, eating, climbing, shift, and mean of latitudes)

# Group Name and Section
Project Group 6, Section 2

# UNI of Each Memeber
xj2242, xw2675
# App link
https://omega-buckeye-254017.appspot.com/sightings/

