# Hyundai-Remote-Canada
Since Hyundai doesn't have Google Assistant/Home integration in Canada, this is an attempt to make it available via web calls to their portal.

# Notes

*The Hyundai Canada site is pretty slow, so don't expect fast responses.
*This is currently a work in progress. Will remove this note once ready.

# API
## Lock
GET http://<address or domain>:<port>/lock
## Unlock
GET http://<address or domain>:<port>/unlock

# Status
## Working
- Single car via configuration file
- Unlock/Lock car
- Docker container
## Todo
- Get vehicle status
- Start car
- Start car with profile (set temperature, etc.)
- Stop car
- Docker entrypoint to handle config through env vars
- API endpoint security (TBD: let user handle via API gateway or include key handling?)
