

## Full Stack Capstone

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

This app without frontend , you can use it using CURL or [Postman](https://www.postman.com/)



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

Base URL: is  https://capstone2fsnd.herokuapp.com/

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

Use this link to enter app , first Auth0 login page: [Clik here](https://bdoor-coffee.us.auth0.com/authorize?
audience=capstone&
response_type=token&
client_id=VhjpGexG9k4U7gHF6KEb0jyaQLedFgpr&
redirect_uri=https://capstone2fsnd.herokuapp.com/)



## Deployment

The API is deployed on Heroku : [here](https://capstone2fsnd.herokuapp.com/)

## Endpoints

- **Use Postman to test each endpoints :**

  **GET** `'\actors'` Fetches all actors in database

  - CURL  `'https:\\capstone2fsnd.herokuapp.com\actors' `with Casting_Assistant token
  - Example 

  ```javascript
  {
      "Actors": [
          {
              "age": "20",
              "gendar": "female",
              "id": 1,
              "movies": [],
              "name": "Amal"
          },
          {
              "age": "21",
              "gendar": "female",
              "id": 2,
              "movies": [],
              "name": "Sara"
          },
          {
              "age": "18",
              "gendar": "female",
              "id": 3,
              "movies": [],
              "name": "Samer"
          },
          {
              "age": "18",
              "gendar": "male",
              "id": 4,
              "movies": [],
              "name": "Omar"
          },
          {
              "age": "32",
              "gendar": "male",
              "id": 5,
              "movies": [],
              "name": "Osama"
          }
      ],
      "success": true
  }
  ```

- **GET** `'\actors\actor_id'` Fetches specific actor  in database

  - CURL  `'https:\\capstone2fsnd.herokuapp.com\actors\1' `with Casting_Assistant token
  - Example 

```javascript
{
    "Actors": [
        {
            "age": "20",
            "gendar": "female",
            "id": 1,
            "movies": [],
            "name": "Amal"
        }
    ],
    "success": true
}
```

- **GET** `'\movies'` Fetches all movies in database

  - CURL  `'https://capstone2fsnd.herokuapp.com/movies' `with Casting_Assistant token
  - Example 

  ```javascript
  {
      "movies": [
          {
              "actors": [],
              "id": 1,
              "release_data": "03/3/2020",
              "title": "first movie"
          },
          {
              "actors": [],
              "id": 2,
              "release_data": "10/1/2020",
              "title": "second movie"
          },
          {
              "actors": [],
              "id": 3,
              "release_data": "12/3/2020",
              "title": "third movie"
          },
          {
              "actors": [],
              "id": 4,
              "release_data": "23/5/2020",
              "title": "fourth movie"
          },
          {
              "actors": [],
              "id": 5,
              "release_data": "13/7/2020",
              "title": "Fifth movie"
          }
      ],
      "success": true
  }
  ```

- **GET** `'\movies\movie_id'` Fetches specific movie  in database

  - CURL  `'https:\\capstone2fsnd.herokuapp.com\movies\1' `with Casting_Assistant token
  - Example 

```javascript
{
    "movies": [
        {
            "actors": [],
            "id": 1,
            "release_data": "03/3/2020",
            "title": "first movie"
        }
    ],
    "success": true
}
```

- **POST** `'\acotrs'` add new  actor in database
  - CURL  `'https:\\capstone2fsnd.herokuapp.com\actors' `with Casting_Director token
  - Example 

```javascript
{
    "actor": {
        "age": "20",
        "gendar": "female",
        "id": 6,
        "movies": [],
        "name": "Alaa"
    },
    "success": true
}
```

- **POST** `'\movies'` add new  movies in database
  - CURL  `'https:\\capstone2fsnd.herokuapp.com\movies' `with Executive_Producer token
  - Example 

```javascript
{
    "movie": {
        "actors": [],
        "id": 6,
        "release_data": "03/3/2020",
        "title": "six movie"
    },
    "success": true
}
```

- **PATCH** `'\actors\actor_id'` edit  actor information in database
  - CURL  `'https:\\capstone2fsnd.herokuapp.com\actors\6' `with Casting_Director token
  - Example 

```javascript
{
    "actor": [
        {
            "age": "20",
            "gendar": "female",
            "id": 6,
            "movies": [],
            "name": "Reem"
        }
    ],
    "success": true
}
```

- **PATCH** `'\moovies\movie_id'` edit  movie information in database
  - CURL  `'https:\\capstone2fsnd.herokuapp.com\movies\4' `with Casting_Director token
  - Example 

```javascript
{
    "movie": [
        {
            "actors": [],
            "id": 4,
            "release_data": "03/3/2020",
            "title": "seven movie"
        }
    ],
    "success": true
}
```

- **DELETE** `'\actors\actor_id'` delete  actor  in database
  - CURL  `'https:\\capstone2fsnd.herokuapp.com\actors\2' `with Casting_Director token
  - Example 

```javascript
{
    "delete": 2,
    "success": true
}
```

- **DELETE** `'\moovies\movie_id'` delete  movie  in database
  - CURL  `'https:\\capstone2fsnd.herokuapp.com\movies\3' `with Executive_Producer token
  - Example 

```javascript
{
    "delete": 3,
    "success": true
}
```



### Error Handlers

Errors are returned as JSON in format:

```
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404
```

- `400:Bad Request`
- `404:resource not found`
- ` 403:permission not allowed`
- ` 422:unprocessable`



## Style

The code adheres to the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) 



## API Testing

Create the database for test in Postgres run :

```
CREATE DATABASE capstone_test ;
```

To run Tests :

```javascript
source setup.sh 
python test_app.py
```

