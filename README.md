# NetCDF data extractor
NetCDF (network Common Data Form) is a file format for storing multidimensional scientific data (variables) such as temperature, humidity, pressure, wind speed, and direction.

### ncArea_extract
NetCDF data file management  
This notebook is beginner-friendly and suitable for a range of use cases in modeling data preparation  

This notebook aims following tasks 🥅
- [ ] reading the NetCDF file
- [ ] extracting attributes
- [ ] extracting physical values as arrays
- [ ] display as images
- [ ] display in automatically adjusting frames
- [ ] extract by data range / give area AOI (shapefile)
- [ ] save png images / create gif animations
- [ ] convert into geotiff, so that work easilly with rasterio/GDAL/QGIS/ENVI  
This notebook contains functionality for extracting data from NetCDF files for an area of interest (AOI) and converting them to the text data format for use by grid-based ecosystem models.  
Use case scenario; Boreal Ecosystem Productivity Simulator uses grid-based bin data sets as input weather data files. This code will create data set for a given resolution to match the spatial resolution of the satellite sensor ✔️  

Readings

[NOAA](https://www.weather.gov/abrfc/map) - learn precipitation measurement techniques  
[NASA](https://www.giss.nasa.gov/tools/panoply/) Panoply netCDF, HDF, and GRIB Data Viewer


### 
This python file contains the necessary functions to extract data from a netCDF file.
It will create a time series plot and output data in a CSV file. In addition, metadata attributes also can be visualized for the file.  
  
  
input: NetCDF, day, lat, long   
output: TS plot and CSV                          


![download](https://user-images.githubusercontent.com/25448193/199521909-98f933e7-6a66-423e-82b1-8c3aab165268.png)


Panoply desktop software works best for quick views and creating animation using NetCDF files. Python packages, xarray, and NetCDF4 work best for modeling and production environments.
Follow this link to Panoply by NASA.  
(https://www.giss.nasa.gov/tools/panoply/)
![precipitation_amount_in_pr_2021](https://user-images.githubusercontent.com/25448193/189524681-00c27ce1-5f8f-4ac4-b510-19880acf64e0.png)

Following image illustrates the gif output of the extracted data. Users can generate this with different visual parameters.

![animatedPrecep](https://user-images.githubusercontent.com/25448193/199523289-2f9a5ba1-ffdf-4f5b-85df-847209dc4d9c.gif)

