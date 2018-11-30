[![Build Status](https://travis-ci.com/bafiam/iRepoter-api.svg?branch=develop)](https://travis-ci.com/bafiam/iRepoter-api)

# iReporter API - Challenge 2
Corruption is a huge bane to Africa’s development. African countries must develop novel and
localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables
any/every citizen to bring any form of corruption to the notice of appropriate authorities and the
general public. Users can also report on things that needs government intervention

## Run the server
1. Next is to start the server with the command `python run.py`
       The server should be running on [http://127.0.0.1:5000]
       
# Usage
     Use Postman (a Google chrome extension for api testing).
     
### API Endpoints
| API Endpoint | Functionality |
| -----------  | ------------- |
| POST /register |  Register a new user |
| POST /login |  Login in a user |
| GET /red_flag_records |  Fetch all accidents |
| POST /red_flag_records |  Create a single accident into the records list|
| DELETE /red_flag_record/<int:id> |  Delete a accident record |
| PUT /red_flag_record/<int:id> |  update a single accident record |
| GET /red_flag_record/<int:id> |  Fetch single accident |

