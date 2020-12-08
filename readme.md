## Asynchronous Group Chat [Real-Time] ![Django](https://img.shields.io/badge/Django-2.2.9-yellow.svg) ![Django](https://img.shields.io/badge/Django%20channels-3.0.2-green.svg)

###### Note: This project is for training on Django-Channels

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Run](#run)

## General info
- This project let's you recieve stock market price and see the changes in the chart real time and no need to refresh the page
- Based on Channels and WebSockets
- The stock prices here are randomly generated through a script and being pushed to the websocket

## Technologies
Project is created with:
* Django: 2.2
* Django Channels: 3.0
* Twisted: 20.3
	
## Run
To run this project, install it locally and make sure to install the twisted version that can run with your os with no problem
Here is the Twisted v20.3.0 for windows, You will find the file in the repo

```
$ pip install requirements.txt
$ python manage.py runserver
```

After running the server make sure to run the redis server located inside [redis/redis-server.exe]
