# Micro
Microservices application for receiving real-time cryptocurrency rates from www.coingecko.com
# How it works?
Precondition: Docker is installed.
1. Download this repository by clicking "Code" -> "Download ZIP" or clone the repository with the command:
   `https://github.com/AlexandraLos/micro.git`
2. Open the "api_micro" folder in a terminal and run the following commands:
`sudo docker build -t api:v0.1 api/`, `sudo docker run --net=host api:v0.1`
3. Open the "db_micro" folder in a terminal and run the following commands:
`sudo docker build -t db_api:v0.1 db/`, `sudo docker run --net=host db_api:v0.1`
4. Open the "app_micro" folder in a terminal and run the following commands:
`sudo docker build -t my_api:v0.1 app/`, `sudo docker run --net=host my_api:v0.1`
5. Run the application "app.py": `python3 app.py`
# How do I choose the cryptocurrency I need?
To change cryptocurrencies, go to www.coingecko.com, find the required cryptocurrency and enter its name in the 6th line of the app->app _micro->"app.py" file.