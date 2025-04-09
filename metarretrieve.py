from awips.dataaccess import DataAccessLayer
from datetime import datetime, timedelta

# Set EDEX server
edex_url = "http://edex-cloud.unidata.ucar.edu"
DataAccessLayer.changeEDEXHost(edex_url)

# Create a METAR request
request = DataAccessLayer.newDataRequest("obs")
request.setParameters("stationId", "temperature", "windSpeed", "windDir", "report")
request.setLocationNames("KDEN")  # Denver International Airport

# Set time range (last 30 minutes)
end_time = datetime.utcnow()
start_time = end_time - timedelta(minutes=30)
request.setTimeRange(start_time, end_time)

# Fetch the data
response = DataAccessLayer.getGeometryData(request)

# Print METAR details
for data in response:
    station = data.getString("stationId")
    temp = data.getNumber("temperature")
    wind_speed = data.getNumber("windSpeed")
    wind_dir = data.getNumber("windDir")
    report = data.getString("report")
    time = data.getDataTime()
    print(f"Station: {station}")
    print(f"Time: {time}")
    print(f"Temperature: {temp}°C")
    print(f"Wind: {wind_speed} m/s from {wind_dir}°")
    print(f"METAR: {report}")
    print("-" * 50)
