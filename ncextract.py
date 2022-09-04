######################################################################################
# This file contains necessary functions to extract data from a netCDF file. It will #
# will  create a time series plot and output data in a csv file                      #
# input: netcdf, day, lat, lon output: TS plot and csv                               #
# Author: Yahampath Marambe 2022-09-03                                               #
######################################################################################

# import libraries
from socket import create_server
from turtle import color, title
import numpy as np
import xarray as xr
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
# nearest mid point
lat = find_nearest_point(precep['precipitation_amount']['lat'].values, lat_of_interest)
lon = find_nearest_point(precep['precipitation_amount']['lon'].values, lon_of_interest)
print('nearest location is lat {} and lon is {}'.format(lat, lon))

# select data for the point
point_data = precep['precipitation_amount'].sel(lat=lat,
                                                lon=lon,
                                                day=slice(start, end))
# plotting Time Sieries
# precipitation data
precep_y = point_data
# time line
day_x = point_data['day']
# figure declaration
fig, (ax1) = plt.subplots(figsize=(16,4))
# plot chart
ax1.bar(day_x, precep_y,
        width=0.5, color = 'purple')
# tittle
ax1.set(title='Precipitation Time Series - point sampling')
# axis lables
plt.xlabel('Day')
plt.ylabel('Precipitation(mm)')
# month location
months = mdates.MonthLocator()
# days location
days = mdates.DayLocator()
# months format when display
monthFmt = mdates.DateFormatter('%b')
# set locators to axis
ax1.xaxis.set_major_locator(months)
ax1.xaxis.set_minor_locator(days)
# set display day formatter to axis
ax1.xaxis.set_major_formatter(monthFmt)
# set x axis limits
ax1.set_xlim(day_x.min(), day_x.max())
# x tick rotation
plt.xticks(rotation=50)
plt.savefig('./output/TS_plot.png')
plt.show()
