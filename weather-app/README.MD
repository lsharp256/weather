This app receives weather data from `http://weather.news24.com/sa/capetown`
and displays it. 

**How to use app:**

Create a psql database called '**weather_db**'.

'`createdb weather_db`'

After connecting to the database, install 'requirements.txt'
with '`pip install -r requirements.txt`'

Navigate to weather_main folder and 
run the following commands:

`python manage.py migrate`

`python manage.py runserver`

To populate the database with weather data run:

`python manage.py get_weather`

Navigate to 127.0.0.1:8000 in the browser and create a profile. A superuser can
be created to view the weather and user data in the admin panel.

 
Navigate to 127.0.0.1:8000/api to view the the data in JSON format 
(User needs to be logged in).