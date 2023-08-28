
# voting backend django rest apis

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Tharwat99/voting_backend_django.git
$ cd voting_backend_django
```
You Should also create a .env file and add these variables below inside it to Create an SMTP connection to Gmail:

```sh
$ USER_NAME = 'your Gmail account here
$ PASSWORD = 'your Gmail apps password here'
```
Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt

```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Then makemigrations and migrate models to sqlite db:
```sh
(env)$ python manage.py makemigrations 
(env)$ python manage.py migrate
```
```
Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test
```
