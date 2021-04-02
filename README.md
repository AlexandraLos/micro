# Micro
Microservices application for receiving real-time cryptocurrency rates from www.coingecko.com
# How it works?
Precondition: Docker is installed.
1. Download this repository by clicking "Code" -> "Download ZIP" or clone the repository with the command:
   `https://github.com/AlexandraLos/micro.git`
2. Open the project folder and run the build:
   `docker-compose build`
3. Start containers with the command:
   `docker-compose up`
4. Make a request in the search bar of your browser by substituting the value of the desired currency instead of "tiker", for example "bitcoin":
   `http://127.0.0.1:8080/myapi/{tiker}`
# How do I choose the cryptocurrency I need?
To change cryptocurrency, go to www.coingecko.com, find the required cryptocurrency and follow the instructions from point 4.