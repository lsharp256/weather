from django.core.management.base import BaseCommand
from weather_app.models import Weather

from datetime import datetime
import requests
import json




class Command(BaseCommand):
    help = 'running this script will populate the database with weather data.'

    def handle(self, *args, **options):
        url = "http://weather.news24.com/ajaxpro/Weather.Code.Ajax,Weather.ashx"

        headers = {'X-AjaxPro-Method': 'GetForecast7Day'}

        payload = {"cityId": "77107"}

        r = requests.post(url, headers=headers, data=json.dumps(payload))
        weather_data = r.json()
        year = str(datetime.today().year)

        for forecast in weather_data['value']['Forecasts']:

            week_day = forecast['FormattedDate'] + ' ' + year
            wind_speed = forecast['WindSpeed']
            high_temp = forecast['HighTemp']
            low_temp = forecast['LowTemp']
            rainfall = forecast['Rainfall']

            # Tue, Jan 29

            week_day = datetime.strptime(week_day, '%a, %b %d %Y')

            data_entry = Weather(date=week_day, wind_speed=wind_speed,
                                 high_temp=high_temp, min_temp=low_temp, rain=rainfall)
            data_entry.save()
