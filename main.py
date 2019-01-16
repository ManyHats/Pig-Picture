from google_images_download import google_images_download
from random import randint
from urllib.request import urlretrieve
from datetime import datetime
import ctypes
import os
import random

# Seed Random
random.seed(datetime.now())

# Google image download init
response = google_images_download.googleimagesdownload()

# Set random offset to pick image
offset = randint(0, 49)

# Set Arguments
arguments = {"keywords":"pigs", "limit":"50", "size":">2MP", "aspect_ratio":"wide", 
            "type":"photo", "format":"jpg", "image_directory":"pigs", "no_download":True}

# Pass in arguments
paths = response.download(arguments)

# Get random image to download
url = list(paths.values())[0][offset]

# Download image from url
urlretrieve(url, "downloads/pigs/pig.jpg")

# Set Desktop Background
def _set_Background():
    SPI_SETDESKWALLPAPER = 20 
    dir = os.path.dirname(os.path.realpath(__file__))
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, dir + "/downloads/pigs/pig.jpg" , 0)
    #os.remove("pig.jpg")

# Set background
_set_Background()

print(offset)
print(url)
