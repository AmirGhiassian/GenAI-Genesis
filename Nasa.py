import os
from io import BytesIO
from skimage import io
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import urllib.request
import urllib.parse
import mapbox_vector_tile
import xml.etree.ElementTree as xmlet
import lxml.etree as xmltree
from PIL import Image as plimg
import numpy as np
from owslib.wms import WebMapService
from IPython.display import Image, display
import math


class Nasa:

    def __init__(self):
        self.layers = {
            "Chlorophyll": {
                "layer": "MODIS_Aqua_L2_Chlorophyll_A",
                "style": "default",
                "Tile_Matrix_Set": "1km",
                "Img_Type": "png",
            },
            "DaytimeSST": {
                "layer": "MODIS_Aqua_L2_Sea_Surface_Temp_Day",
                "style": "default",
                "Tile_Matrix_Set": "1km",
                "Img_Type": "png",
            },
            "NighttimeSST": {
                "layer": "MODIS_Aqua_L2_Sea_Surface_Temp_Night",
                "style": "default",
                "Tile_Matrix_Set": "1km",
                "Img_Type": "png",
            },
            "PAR": {
                "layer": "MODIS_Aqua_L2_Photosynthetically_Available_Radiation",
                "style": "default",
                "Tile_Matrix_Set": "1km",
                "Img_Type": "png",
            },
        }
        print("I Ran!")
        self.TILE_MATRIX = 2

    def change_style(self, layer, style):
        self.layers[layer]["style"] = style

    @classmethod
    def default_config(self):
        self.__init__(self, "default", 2)

    @classmethod
    def time_config(self, time):
        self.__init__(self, time, 2)

    def get_layers(self):
        return self.layers.keys()

    def set_time(self, time):
        self.time = time

    def set_cordinates(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.TILECOL = math.floor((longitude + 180) / 360 * 2**self.TILE_MATRIX)

        self.TILEROW = math.floor(
            (
                1
                - (
                    math.log(
                        math.tan(math.radians(latitude))
                        + 1 / math.cos(math.radians(latitude))
                    )
                    / math.pi
                )
            )
            * 2 ** (self.TILE_MATRIX - 1)
        )

    def get_image(self, layer):
        self.layer = layer
        satalite_image = (
            f"https://gitc.earthdata.nasa.gov/wmts/epsg4326/best/%s/%s/%s/%s/%s/%s/%s.%s"
            % (
                self.layers[layer]["layer"],
                self.layers[layer]["style"],
                self.time,
                self.layers[layer]["Tile_Matrix_Set"],
                self.TILE_MATRIX,
                self.TILEROW,
                self.TILECOL,
                self.layers[layer]["Img_Type"],
            )
        )
        print(satalite_image)
        response = requests.get(satalite_image)
        img = plimg.open(BytesIO(response.content))
        return img

    def show_image(self, layer):
        plt.imshow(self.get_image(layer))
        plt.show()
