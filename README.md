[![Build Status](https://travis-ci.com/bafiam/iRepoter-api.svg?branch=develop)](https://travis-ci.com/bafiam/iRepoter-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/7da98dcd5b7420e1ad71/maintainability)](https://codeclimate.com/github/bafiam/iRepoter-api/maintainability)
[![codecov](https://codecov.io/gh/bafiam/iRepoter-api/branch/develop/graph/badge.svg)](https://codecov.io/gh/bafiam/iRepoter-api)

# iReporter API - Challenge 3
Corruption is a huge bane to Africa’s development. African countries must develop novel and
localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables
any/every citizen to bring any form of corruption to the notice of appropriate authorities and the
general public. Users can also report on things that needs government intervention

## Prerequisites
The development environment uses postgres db, hence install postgres before proceeding.
    - Mac OS - `brew install postgresql`
    - linux - `sudo apt-get install postgresql postgresql-contrib`
    - windows - Download postgres [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows)

Once installed create a database named `ireporter`
(for linux and mac OS users)
1. type `psql` in terminal.
2. On postgres interactive interface, type `CREATE DATABASE ireporter;`
3. Grant privileges to the user by typing `GRANT ALL ON DATABASE ireporter to <your-postgres-username>;`
## Installation and set-up
1. Clone the project - `git@github.com:bafiam/iRepoter-api.git`
2. create a virtual environment using virtualenv.
3. Install the dependencies - `pip install -r requirements.txt`.

## Run the server
1. Next is to start the server with the command `python run.py`
       The server should be running on [http://127.0.0.1:5000]
       
## Testing
The tests have been implemented using `pytest`
 To run: Type
        `pytest --cov=./app -v`
        on your Terminal to get a report.
        
## Testing the endpoints
Use `POSTMAN` after running the app using `python run.py
   
        
## Documentation
iReporter documentation [here](https://documenter.getpostman.com/view/987109/Rzfgnori)   
# Usage
     Use Postman (a Google chrome extension for api testing).
     
### API Endpoints
| API Endpoint | Functionality |
| -----------  | ------------- |
| POST /auth/register |  Register a new user |
| POST /auth/login |  Login in a user |
| PATCH /profile/`<username>` |  Add more user information |
| GET /incidences |  Fetch all incident |
| POST /incidences  |  Create an incident record|
| GET /incidences/`<id>` |  Fetch single incident record|
| DELETE /incidences/`<id>` |  Delete a incident record |
| PATCH /incidences/`<id>` | Update a incident record image and video |
| PATCH /incidences/update/`<id>` | Update a incident record comment or location based on createdby|
|PATCH /admin/incidences/update/status/`<id>` | Admin update a incident record status |

 ### Heruko [here](<https://stephen-ireporter.herokuapp.com/api/v1/>)
