# -*- coding: utf-8 -*-
### The code gets the data from weather API (OWM) and sends tweets about about the temperature

import tweepy 
import time, os, sys
from dotenv import Dotenv
import pyowm
from random import randint

# The sensitive data is written in the .env file, in the format KEY='KEY'
# Dotenv helps to get the data from the local folder, otherwise the computer will get some other .env
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env")) # get the .env file from your folder
os.environ.update(dotenv) # update dotenv

# Authorisation in twitter
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth) # authentification

# Authorisation in OpenWeatherMap

OWM_key = os.environ['OWM_KEY'] # put your access code here
owm = pyowm.OWM(OWM_key) 

# The body of the code (in a loop, so it always computes. Just remove 'while' if you test it from the computer.)

while True:
    cityfile = open("cityid.txt", 'r')  # open file with city names, id, locations
    citydata = cityfile.readlines()  # read every line
    len_citydata = len(citydata)  # how many cities we have
    cityline = randint(1, len_citydata) # choose random line
    cityline_split = citydata[cityline].split()
    if len(cityline_split) == 5: # city is a single word
        cityname = cityline_split[1]
    else: # when the city is not a single word ("New York"), the array has more than 5 elements so we just take all extra
        cityname = cityline_split[1]
        for x in range(2, len(cityline_split) - 3):
            cityname = cityname + " " + str(cityline_split[x])
    cityfile.close() # to be sure, that the file closes. All above could be outside the loop, but then the file is not closed.

    citycountry = cityline_split[len(cityline_split)-1] # country code

    observation = owm.weather_at_place(cityname)
    # also can use weather_at_id, weather_at_coords
    w = observation.get_weather() # get weather data
    weather_status = w.get_detailed_status() # there is also an option get_status
    temperature = w.get_temperature('celsius') # there are 4 fields: temp_max, temp_kf, temp, temp_min

    # now compose the message with the retrieved data
    message = "The temperature in " + str(cityname) + ", " + str(citycountry) + " is " + str(int(temperature['temp_max'])) + "℃. " + "And, well, " + str(weather_status) + "."

    # send the message to twitter and sleep for 2 hours
    api.update_status(message)
    time.sleep(7200) 
