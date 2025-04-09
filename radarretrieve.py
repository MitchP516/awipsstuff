import matplotlib.pyplot as plt
from awips.dataaccess import DataAccessLayer
from datetime import datetime, timedelta
import cartopy.crs as ccrs

# Set EDEX server
edex_url = "http://edex-cloud.unidata.ucar.edu"
DataAccessLayer.changeEDEXHost(edex_url)

# Create a radar data request
request = DataAccessLayer.newDataRequest("radar")
request.setParameters("reflectivity")
request.setLocationNames("KTLX")  # Example radar site: Oklahoma City

# Set time range (last 15 minutes)
end_time = datetime.utcnow()
start_time = end_time - timedelta(minutes=15)
request.setTimeRange(start_time, end_time)

# Fetch the data
response = DataAccessLayer.getGeometryData(request)

# Extract latitude, longitude, and reflectivity
lats = [data.getGeometry().y for data in response]
lons = [data.getGeometry().x for data in response]
refl = [data.getNumber("reflectivity") for data in response]

# Create a plot
plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
scatter = ax.scatter(lons, lats, c=refl, cmap="jet", s=50, transform=ccrs.PlateCarree())
plt.colorbar(scatter, label="Reflectivity (dBZ)")
plt.title(f"Radar Reflectivity for KTLX - {end_time.strftime('%Y-%m-%d %H:%M UTC')}")
plt.show()
