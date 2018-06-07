## maintenance tracker api

[![Build Status](https://travis-ci.org/lytes20/bootcamp-challenge-3.svg?branch=ch-cicd)](https://travis-ci.org/lytes20/bootcamp-challenge-3)
[![Coverage Status](https://coveralls.io/repos/github/lytes20/bootcamp-challenge-3/badge.svg?branch=master)](https://coveralls.io/github/lytes20/bootcamp-challenge-3?branch=master)

## About
This is an API for a maintenance tracker application that allows users to make maintenance or repair requests and monitor them
## Features
- Register a user
- Login a user
- Get all the requests for a logged in user
- Get a request for a logged in user
- Create a request.
- Modify a request
- Approve a request
- Disapprove a request
- Resolve a request
## Tools Used
- [Flask](http://flask.pocoo.org/) - web microframework for Python
- [Virtual environment](https://virtualenv.pypa.io/en/stable/) - tool used to create isolated python environments
- [pip](https://pip.pypa.io/en/stable/) - tool used used to install python messages
- [git](https://git-scm.com/) - free open source distributed version control system
## Requirements
Python 3.x.x+
## Run (Use) on your local machine
First clone the repository
```sh
   $ git clone https://github.com/lytes20/maintenance-tracker-api.git
   ```
   Head over to the cloned directory, create a virtual environment, use pip to install the requirements, the run the app
   ```sh
    $ cd maintenance-tracker-api
    $ virtualenv venv
    $ source venv/Scripts/activate
    $ pip install -r requirements.txt
    $ python run.py
```
#### Endpoints to create a user account and login into the application
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | api/v1/user/register | True | Create an account
POST | api/v1/user/login | True | Login a user

#### Endpoints to create, read and update user requests
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | api/v1/users/requests | True | Create a request
GET | api/v1/users/requests | False | Fetch requests for a logged in user
GET | api/v1/users/requests | False | Fetch requests for a logged in user
GET | api/v1/users/requests/requestid | False | Fetch a request for a logged in user
PUT | api/v1/users/requests/requestid | False | Update a request for a logged in user
PUT | api/v1/requests/requestId/approve | False | Approve a user request
PUT | api/v1/requests/requestId/disapprove | False | disapprove a user request
PUT | api/v1/requests/requestId/resolve | False | resolve a user request

## Authors
[Bamuleseyo Gideon](https://github.com/lytes20)