# RedditCrawler

*    Title: Drones API    
*    Author: Guillem Alomar      
*    Initial release: August 7th, 2019                     
*    Code version: 0.1                         
*    Availability: Public     

**Index**
* [Documentation](#documentation)
    * [Explanation](#explanation)
    * [Project Structure](#project-structure)
* [Using the application](#using-the-application)
    * [Requirements](#requirements)
    * [First of all](#first-of-all)
    * [Running the server](#running-the-server)
    * [Executing the client application](#executing-the-client-application)
* [Decisions taken](#decisions-taken)

## Documentation

### Explanation

This project consists in a Drones API. Users can see and manipulate the information uploaded to the API DB.

### Project Structure

It's not complex at all. All information is obtained only from users through endpoints, and stored in a SQL DB. Then that information can be read also through endpoints.

## Using the application

### Requirements

- Python +3.7

The complete list of packages is available in the file _requirements.txt_

### First of all

- I recommend creating a virtualenv for this project. After creating it and activating it, you should run:
```
~/DronesAPI$ pip install -r requirements.txt
```

Now all pip packages needed have been installed.

To be able to create admin users, a user must have a secret key which can be specified in the _creds.py_ file. This file can be created from the _creds_dummy.py_ file with your own key.

### Running the server

First of all, the user should start by running the server with Gunicorn. This is done this way:
```
~/DronesAPI$ gunicorn -w 4 -b 127.0.0.1:5000 rest_api:app
```

If this has worked correctly, this should be the output:`
```
[2019-08-07 12:40:22 +0800] [51020] [INFO] Starting gunicorn 19.9.0
[2019-08-07 12:40:22 +0800] [51020] [INFO] Listening at: http://127.0.0.1:5000 (51020)
[2019-08-07 12:40:22 +0800] [51020] [INFO] Using worker: sync
[2019-08-07 12:40:22 +0800] [51023] [INFO] Booting worker with pid: 51023
[2019-08-07 12:40:22 +0800] [51024] [INFO] Booting worker with pid: 51024
[2019-08-07 12:40:22 +0800] [51025] [INFO] Booting worker with pid: 51025
[2019-08-07 12:40:22 +0800] [51026] [INFO] Booting worker with pid: 51026
```

The server can also be executed with a single thread by running:
```
~/DronesAPI$ python rest_api.py
```

### Executing the client application

Now that the server is running, we can execute an application that encapsulates the calls to the API, for an easier usage. This is done by typing this:
```
~/DronesAPI$ python testing_application.py
```

## Decisions taken

To do this project I followed some basic instructions, but the specific components and architecture had to be chosen by me.

- Authentication system

This wasn't the first time I implemented a RESTful API (see https://github.com/guillemalomar/RedditCrawler, https://github.com/guillemalomar/SongsPlatform), and neither that I used a SQL database. But it was the first time that I used any type of authentication system. I had worked with Flask before but always at internal level, where no user profiles were needed.

- Database

When choosing the database I decided to use SQL Alchemy after also pondering about MongoDB (which I know from doing some MongoUniversity courses, and tinkering with it for one of my projects: https://github.com/guillemalomar/GeneticAlgorithm). I decided to use the first one because it's the one that fits better with Flask, and for this project I didn't have enough time to implement the MongoDB connection (maybe with a few more hours). For production scale, SQL Alchemy wouldn't even be an option. Mongo would also be a good option because it can graph geolocation data, and drones are quite related to that.

- User registration

Currently, only users from the Support team can execute commands that involve registering new drones and cameras, and deleting users, drones and cameras. Also, support users can only be created by using a specific key. This key can be specified in the _creds.py_ file (which I haven't added to the project, as credentials should never be uploaded to online repositories). I don't know if this would be the best way to do this, but i think it's a safe way, as this way the users with more power can be created safely, and other types of users will never be able to create users (which makes sense to me).

- Drone registration and cameras data

There is a thing that I had to consider when modeling the API data. Drones contain a list of possible cameras. I decided to create another table only for cameras data. This way, whenever a drone has to be registered, the API checks if all the drones specified camera models exist as a registered camera, and otherwise it will not register the drone. This way I can also easily obtain the cameras information without having to check all drones (which I guess would be stored in a much bigger table).

- Testing

I always make tests for my codes, but in this case I don't have the knowledge do them taking into account the logged users keys. If I knew that I would create a test for each endpoint and resource method, with a new database only for that. If I had to work more on the project, I would modify the git hook to avoid being able to do commits unless all tests passed.

- Deployment

I have previously deployed this kind of servers using Jenkins, and it's what I would propose to do as it's for an internal server.
I don't think this would have to store and deliver enough data to justify having a QA deployment for testing. The methods would be also quite fixed, from the specifications it doesn't seem that it would change often.