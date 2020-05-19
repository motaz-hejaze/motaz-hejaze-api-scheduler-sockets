# Api-fetcher

requirements:
-----------------
  - python >= 3.6
  - virtualenv
  - Git
------------------

* first clone the repo:
  - git clone https://github.com/motaz-hejaze/motaz-hejaze-api-scheduler-sockets.git


* cd into cloned folder:
  - cd motaz-hejaze-api-scheduler-sockets

* create virtual environmet:
  - virtualenv venv -p python3.6
  
* activate your virtual environment:
  - source venv/bin/activate (linux)

* install required python packages:
  - cd project
  - pip install -r requirements.txt

* create database and tables:
  - python manage.py makemigrations
  - python manage.py migrate

* create superuser:
  - python manage.py creasuperuser

* runserver:
  - gunicorn -k eventlet -w 1 project.wsgi:application

* within your browser , go to http://127.0.0.1:8000/
