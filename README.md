Overview
These scripts are designed for meteorologists, developers, or enthusiasts working with AWIPS data. They leverage the python-awips library to connect to an EDEX server (e.g., Unidata's public server) and process weather data. The scripts include:

Surface Temperature Retrieval: Fetches temperature data for specified stations.
Radar Reflectivity Plot: Visualizes radar reflectivity data on a map.
METAR Data Retrieval: Extracts METAR reports for a given station.

Prerequisites
  Python 3.x: Ensure Python is installed on your system.
  EDEX Server Access: A working connection to an AWIPS EDEX server (default uses http://edex-cloud.unidata.ucar.edu).
  
Dependencies:
  python-awips: Core library for AWIPS data access.
  matplotlib and cartopy (for plotting in Script 2).
Installation
  Install Python: Download and install Python from python.org if not already installed.
  Verify Installation: Run python -c "import awips; print(awips.__version__)" to confirm python-awips is installed.

  Scripts
1. surface_temp.py
Description: Retrieves surface temperature observations for specified weather stations over the last hour.
Parameters: Station IDs (e.g., KJFK, KORD), temperature.
Output: Prints station name, temperature, and observation time.
2. radar_reflectivity.py
Description: Fetches and plots radar reflectivity data for a specified radar site over the last 15 minutes.
Parameters: Radar site (e.g., KTLX), reflectivity.
Output: A Matplotlib plot with a color-coded reflectivity map.
3. metar_data.py
Description: Retrieves METAR reports for a specified station over the last 30 minutes.
Parameters: Station ID (e.g., KDEN), temperature, wind speed, wind direction, raw METAR report.
Output: Prints detailed METAR information.
Usage
Clone or Download: Obtain the scripts from this repository.
Edit Configuration (optional):
Replace the EDEX URL (http://edex-cloud.unidata.ucar.edu) with your local server if applicable.
Update station IDs or time ranges as needed.

Customization: 
Station IDs: Replace with valid ICAO codes (e.g., KSEA for Seattle) or radar site codes.
Time Range: Adjust timedelta values to change the data window (e.g., hours=2).
Parameters: Add or modify requested parameters (e.g., pressure, dewpoint) in the setParameters call.
Troubleshooting: 
Connection Errors: Verify the EDEX URL and your internet connection. The default server may occasionally be unavailable.
Missing Data: Ensure the station ID and parameters are valid for the chosen data type.
Plotting Issues: Confirm matplotlib and cartopy are installed correctly.
Contributing
Feel free to submit pull requests or issues for improvements, bug fixes, or additional script ideas!

License: 
This project is unlicensed and free for use. It is provided "as is" with no warranties.
