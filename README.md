# RedditCrawler

*    Title: Drones API    
*    Author: Guillem Alomar      
*    Initial release: August 6th, 2019                     
*    Code version: 0.1                         
*    Availability: Public     

**Index**
* [Requirements](#requirements)
* [Documentation](#documentation)
    * [Project Structure](#project-structure)
    * [Explanation](#explanation)
* [Using the application](#using-the-application)
    * [Executing](#executing)
    * [Testing](#testing)
* [Decisions taken](#decisions-taken)

## Requirements

- Python 2.7 (not tested on python3, at least the prints should be removed) 
- lib xml (lxml): pip install lxml
- Web.py: pip install web.py
- Praw: pip install praw==3.6.0
- Unidecode: pip install unidecode

## Documentation

### Explanation

This project consists in a Drones API. Users can see and manipulate the information uploaded to the API DB.

### Project Structure

- Application Architecture

![alt text][logo]

[logo]: https://github.com/guillemnicolau/RedditCrawler/blob/master/documentation/ApplicationArchitecture.png?raw=true "Application Architecture"

## Using the application

### First of all

- I recommend creating a virtualenv for this project. After creating it and activating it, you should run:
```
~/DronesAPI$ pip install -r requirements.txt
```
Now all pip packages needed have been installed.

### Executing

- Running the server

First of all, the user should start by running the server. This is done this way:
```
~/DronesAPI$ python src/DronesAPI/rest_api.py
```
If this has worked correctly, this should be the output:`
```
http://localhost:5000/
```

- Executing the client application

Now that the server is running, we can execute an application that encapsulates the calls to the API, for an easier usage. This is done by typing this:
```
~/DronesAPI$ python DataApp/application.py
```

## Decisions taken

To do this project I followed some basic instructions, but the specific components and architecture had to be chosen by me.
This wasn't the first time I implemented a RESTful API (see https://github.com/guillemalomar/RedditCrawler, https://github.com/guillemalomar/SongsPlatform), and neither that I used a SQL database. But it was the first time that I used any type of authentication system. I had worked with Flask before but always at internal level, where no user profiles were needed. My implementation is probably not the most efficient want or the most secure one, and I would love to know how it could be done in a better way.

- Database

When choosing the database I decided to use SQL Alchemy after pondering between the mentioned one, MongoDB (which I know from doing some MongoUniversity courses, and tinkering with it for one of my projects: https://github.com/guillemalomar/GeneticAlgorithm). I decided to use the first one because it's the one that fits better with Flask, and for this project I didn't have enough time to implement the MongoDB connection (maybe with a few more hours). For production scale, SQL Alchemy wouldn't even be an option.
