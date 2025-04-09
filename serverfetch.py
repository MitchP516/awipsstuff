from awips.dataaccess import DataAccessLayer
from datetime import datetime, timedelta

# Set the EDEX server (public Unidata server as an example)
edex_url = "http://edex-cloud.unidata.ucar.edu"
DataAccessLayer.changeEDEXHost(edex_url)

# Define the data request
request = DataAccessLayer.newDataRequest("obs")  # Observation data
request.setParameters("temperature")  # Request temperature parameter
request.setLocationNames("KJFK", "KORD")  # Example stations: JFK and O'Hare airports

# Set a time range (last 1 hour)
end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=1)
request.setTimeRange(start_time, end_time)

# Fetch the data
response = DataAccessLayer.getGeometryData(request)

# Print the results
print("Retrieved", len(response), "records")
for data in response:
    station = data.getLocationName()
    temp = data.getNumber("temperature")
    time = data.getDataTime()
    print(f"Station: {station}, Temperature: {temp}°C, Time: {time}")
