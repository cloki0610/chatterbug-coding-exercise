# Chatterbut Coding Exercise

## Features
Develop a Rest API using Fast API that allows users:
 -  To request new password based on length with extra option to use boolean options to control the character pool such as lowercase, uppercase, digits, and symbols.
 - Create an additional endpoint that intigrates a third-party API’s from https://open-meteo.com/.

## Endpoints
### / and /docs (GET)
To use the build-in document page.
### /generate-password (POST)
Endpont to accept form data as payload with following values:
 - length(int) more than 0 and less than 90
 - lowercase(bool)
 - uppercase(bool)
 - digits(bool)
 - symbols(bool)
### /weather (GET)
The endpont accept following query to get the current tempreature:
 - lat(float)
 - long(float)

## Install
### Local environment
1. Use ```git clone``` to clone the project into local directory.
2. Use ```python -m venv ven ``` to create a new local virtual environment.
3. Use ```pip install --no-cache-dir -r requirements.txt``` to install the required package.
4. Use ```uvicorn main:app --reload``` to run the application in local environment.
### Docker
 - Using ```docker compose build``` and ```docker compose up``` to run the container with docker compose.
 - Or Using ```docker build -t <any-image-name>``` to build the image and run it locally.
