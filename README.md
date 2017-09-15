# App Engine Word Cloud

Python app engine web based application. This application is for analyzing custom url like (https://en.wikipedia.org/wiki/Main_Page)
and counts the frequency of use of each word on that page.
Application uses : tornado, torndb

[Demo](https://wordcloud-2017.appspot.com/)

## Installation

Install the [Google App Engine Python SDK](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python).

To run this application on your local machine please follow these steps:
- On your workspace create new folder 'wordcloud_app' and in this folder create a new virtual environment

```bash
virtualenv env

#Then activate it :
source env/bin/activate

git clone https://github.com/esl4m/wordcloud_app.git
cd wordcloud_app

# Install requirements .. just run
pip install -t lib -r requirements.txt

# Create mysql Database , from terminal login to mysql
mysql --user=root --password=

# Then
create database wordcloudapp ;
```

## Running app
```bash
dev_appserver.py
```

## To access the application .. type on your browser
```bash
localhost:8080
```

## To access the admin server .. type on your browser
```bash
http://localhost:8000
```

## To deploy & browse app on appengine :
```bash
gcloud app deploy
gcloud app browse
```

Inspired by [word_cloud](https://github.com/epigos/wordcloud)
