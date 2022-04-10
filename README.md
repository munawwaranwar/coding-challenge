
## Shared Document Store
A project, focused on a RESTful API service rapid prototype development. In this project an API is created that stores “digital documents” in “folders”. Folders or Documents can have one or many associated “Topics”, with short & long-form descriptors.

### Directory & Files structure
This repository contains code for **Shared Document Store** project undertook as a **coding challenge**. Based on Django's MVT model, it contains below structure;

* ``documents_store/settings`` -- The main settings.py file which contains the definition of all project related apps and their initiations   

* ``documents_store/urls`` -- Urls.py contains URLs of all the apps and route to their related urls.py in its respective apps directory

* ``digital_docs/migrations`` -- This Directory contains the DB migration files. These files have details regarding Db models and changes recently occurred in DB Models 

* ``digital_docs/apps`` -- A module that contains the name of the app

* ``digital_docs/admin`` -- A module that registers the models whose details you want to be available on Django-Admin Panel 

* ``digital_docs/models`` -- The main module that contains all the DB Models

* ``digital_docs/views`` -- The Core module which contains all the ViewSets

* ``digital_docs/tests`` -- Main directory which contains modules related to Unit tests and Data. The modules are mentioned below ;
* ``digital_docs/tests/test_models`` -- Module that contains unit tests related to DB Models
* ``digital_docs/tests/test_urls`` -- Module that contains unit tests related to URLs and their resolution to Views functions and classes
* ``digital_docs/tests/test_views`` -- Module that contains unit tests related to ViewSets

* ``digital_docs/serializers`` -- Contains ModelSerializers for all the Django DB-Models


### Prerequisites
In order to run a development environment, [Python 3.9 or higher](https://www.python.org/download/releases/3.0/) and
[Postgresql](https://www.postgresql.org/about/news/1786/) are assumed to be already installed.

it is assumed that all commands mentioned in this guide are run from root directory of the project and inside
```virtual environment```


### Setting up local dev environment
For setting up a local dev environment we assume that the ```prerequisites``` are met already. To setup a local
environment:
* Create database using Postgresql (Name and credentials should be same as in [settings.py](device_notification_subsystem/settings.py))
* Create virtual environment using **virtualenv** and activate it:

To install Virtual Environment Wrapper
```bash
pip install virtualenvwrapper-win
```
To Create Virtual Environment
```bash
mkvirtualenv venv
```
To Activate Virtual Environment
```bash
workon venv
  or
source venv/bin/activate
```
To install Django
```bash
pip install django
```
Go to directory where you want to create the Project
```bash
django-admin startproject documents_store
```
To create app within the project
```bash
python manage.py startapp digital_docs
```
To install required libraries via requirements.txt
```bash
pip install -r requirements.txt
```

To perform DB migrations 
```bash
python manage.py makemigrations
```
To migrate the DB
```bash
python manage.py migrate
```
To create super users
```bash
python manage.py createsuperuser
```
To start the server
```bash
python manage.py runserver 
```
