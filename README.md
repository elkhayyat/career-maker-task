
Career Maker Task
======

This task created for "Career Maker Company"
It is created By Ahmed El-Khayyat


Requirments
--------------
- Docker: https://docs.docker.com/engine/installation/
- Docker-compose: https://docs.docker.com/compose/install/


Installtion
--------------
1- Clone this repository via:

    git clone https://github.com/elkhayyat.career-maker-task

2- Rename .env.bak file to .env

3- Change API_KEY in .env file with your api key - you can get it free from: 
    https://www.alphavantage.co/support/#api-key

4- Build  docker containers using command:
  
    docker-compose build
    
5- Run docker containers using command:

    docker-compose up
  
  

Usage
--------------
** Please note that the API is protected using basic authentication or token authentication.
so you have to create a user before using it.

End Points
--------------
  
    "GET"
    /api/v1/quotes

This API return the latest exchange rate


    "POST"
    /api/v1/quotes
This API refresh fetch the exchange rate from Alphavatage then return it.


## Best Regards
