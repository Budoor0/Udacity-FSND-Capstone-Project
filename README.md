

## Full Stack Capstone

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.



## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to  directory and running:

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) 
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) 
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#)
- [jose](https://python-jose.readthedocs.io/en/latest/) 
- [Gunicorn](https://gunicorn.org/)
- [PostgreSQL](https://www.postgresql.org/)

## Running the server

**To running app locally:** 

In right directory , using virtual environment to run the server : 

```javascript
source setup.sh # file has a token for each role
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```



## API Reference

### Getting Started

Base URL: is  [[[[[[[[[`LINK `]]]]]]]]]

## Roles and Permissions

Currently there are Three users created in AUTH0.com : 

**1- Casting_Assistant:**

- Can view actors and movies

- `get:actors`
- `get:movies`

```
Username : capstone_casting_assistant@gmail.com
Password :capstone_casting_assistant1
```

**2- Casting_Director:**

- Can view actors and movies

- Add or delete an actor from the database

- Modify actors or movies

- `post:actors`

- `delete:actors`

- `patch:actors`

- `patch:movies`

  ```
  Username : capstone_casting_director@gmail.com
  Password :capstone_casting_director1
  ```

**3- Executive_Producer:**

- Can view actors and movies
- Add or delete an actor from the database
- Modify actors or movies
- Add or delete a movie from the database
- `'post:movies'`
- `'delete:movies'`

```
Username : capstone_executive_producer@gmail.com
Password :capstone_executive_producer1
```

## Deployment

The API is deployed on Heroku : 

## Endpoints

 



### Error Handlers

if any errors accured, the API will return a json object in the following format:

```
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404
```

The following errors will be reported:

- `400:Bad Request`
- `404:resource not found`
- ` 403:permission not allowed`
- ` 422:unprocessable`

## API Testing

Create the database for test in Postgres run :

```
CREATE DATABASE capstone_test ;
```

To run Tests :

```
source setup.sh 
python test_app.py
```

