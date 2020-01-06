# Hyundai-Remote-Canada
Since Hyundai doesn't have Google Assistant/Home integration in Canada and it takes 5min to do anything with the official app, this is an attempt to make it available via web calls to their portal.

The goal is to create a service that one can run under docker (I run in GKE), that IFTTT can call, thus allowing voice command. Currently this works for a single car, with lock, unlock, start, and stop functions.

# Notes

- The Hyundai Canada site is pretty slow, so expect remote commands to take around 1min to execute
- This is currently a work in progress
- Some parameters like CARID in docker-compose.yaml file needs to be retrieved from looking at POST data on bluelink website when making a call. This can be resolved using "friendly name" via a small update to the code, which will likely be handled via multi-car capability in the future. (I don't have two cars so if anyone wants to tackle and create pull request, please feel free)
- With minimal development experience and this being my first public project, pardon my sloppy code.
- Constructive criticisms welcome!

# Docker
Substitute values based on your deployment.
## Build
./build.sh
## Run
Remember to create your own docker-compose.yml from example provided.
docker-compose up -d

# API
Substitute values based on your deployment.
## Lock
GET http://localhost:8080/lock
## Unlock
GET http://localhost:8080/unlock
## Start
GET http://localhost:8080/start
## Stop
GET http://localhost:8080/stop

# Authentiation
Submit authentication as "key=<auth_key>" as part of the GET request via x-www-form-urlencoded method for the time being. This works well with IFTTT.

# Status
## Working
- Single car via configuration file
- Unlock/Lock car
- Docker container
- Start car (with hard coded winter profile for now)
- Stop car
- Docker entrypoint to handle config through env vars
- API endpoint security
## Todo
- Get vehicle status
- Support multiple vehicles
- Read remote start profiles
- Start car with profile (set temperature, etc.)
