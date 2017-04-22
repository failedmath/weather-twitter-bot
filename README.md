# weather-twitter-bot
An example of a twitter bot that fetches weather data from OpenWeatherMap. 
It chooses a random city from the list, connects to the OpenWeatherMap and checks the weather.
Working version of the bot (currently not running becuase time for free dynos from Heroku is over) can be found [here] (https://twitter.com/superhotbot). 

# Requirements

- Python 2.7 + packages: tweepy, virtualenv
- Twitter API keys + creating a [twitter app] (https://apps.twitter.com/)
- Heroku account
- OpenWeatherMap API key

# Notes
All the secret keys are written down in the document *.env* in the format KEY='API KEY' for safety.

The requirements can be checked in *requirements.txt*

Heroku is used to run the python code from a server, it has a free dyno for 550 hours per month. Sometimes the dyno has to be turned on manually from the webpage.

# Some useful resources

A little bit on twitter API and Heroku setup can be found [here] (https://github.com/mobeets/twitter-bot-bootstrap)

[Heroku connection] (https://boodoo.co/bletchley.html0

[OpenWeatherMap] (http://openweathermap.org)