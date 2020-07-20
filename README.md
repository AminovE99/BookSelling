# **BookSelling App**

> :alembic: This application provide API create purchase requests for some books.


## :construction: Install

*  Create virtual enviroment for application

```sh
python3 -m venv myvenv
```

* Download packages from requirements.txt

```sh
pip install -r requirements.txt
```

* Configure your redis-server configuration inside `BookSeling.settings`
    * REDIS_HOST - Host of redis
    * REDIS_PORT = Port of redis


## :rocket: Usage
Execute redis-server on your local machine

```sh
redis-server --port REDIS_PORT
```

```sh
python manage.py runserver
```

This service use [Joser](https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints)
authentication system and provide ability to log in to system by JWT Token.

## :white_check_mark: Run tests

```sh
python manage.py test
```
## :bust_in_silhouette: Authors

* [Aminov Emil](https://github.com/AminovE99)


## :zap: Possible Enhancement
* :white_check_mark: Add tests for every view
* :whale: Create docker-compose for app
* :wrench: Configure nginx and add gunicorn server

## :page_facing_up: License

This project is [MIT](uri_license) licensed.