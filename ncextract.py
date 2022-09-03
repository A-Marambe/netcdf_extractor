######################################################################################
# This file contains necessary functions to extract data from a netCDF file. It will #
# will  create a time series plot and output data in a csv file                      #
# input: netcdf, day, lat, lon output: TS plot and csv                               #
# Author: Yahampath Marambe 2022-09-03                                               #
######################################################################################
# import libraries
from socket import create_server
import numpy as np
import xarray as xr
import rioxarray as rxr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

###### change parmeters accordingly
# give start date
start = '2021-05-18'
# give end date
end = '2021-09-04'
# lat , lon of point of interst
lat_of_interest = 33 # 40.367474
lon_of_interest = -90 #-82.996216
##### parameter section ends

# find the nearest point in the grid using given point
def find_nearest_point(location_array, point):
    """
    This function search for the nearest lat from
    a netcdf lat array.
    input: netcdf lat array, lat in mind
    output: nearest  lat
    useage: in this way we can copy the data value nearest to our location
    from the raster, unless xarray raise errors
    """
    idx = np.abs(location_array - point).argmin()
    return location_array[idx]

# netcf location
fn = './input/pr_2021.nc'
# open nc file
precep = xr.open_dataset(fn)
# extract metadata
meta_info = precep.attrs
# print citation; selected metadata
print(meta_info['note2']) 
# see CRS/SRS of the data set
crs_info = precep.rio.crs
print(crs_info)
# print min max of lat and lon
min_lat = precep['precipitation_amount']['lat'].values.min()
min_lon = precep['precipitation_amount']['lon'].values.min()
print('min lat is {} and min lon is {}'.format(min_lat, min_lon))
# print date range
print('from {v1} to {v2}'.format(
                                v1 = precep['precipitation_amount']['day'].values.min(),
                                v2 = precep['precipitation_amount']['day'].values.max()
                                ))
# Extract data
