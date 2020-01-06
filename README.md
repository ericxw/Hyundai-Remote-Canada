# Hyundai-Remote-Canada
Since Hyundai doesn't have Google Assistant/Home integration in Canada, this is an attempt to make it available via web calls to their portal.

# Notes

*The Hyundai Canada site is pretty slow, so don't expect fast responses.
*This is currently a work in progress. Will remove this note once ready.

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
