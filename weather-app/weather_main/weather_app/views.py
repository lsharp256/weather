from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from weather_app.models import Weather
from weather_app.serializer import WeatherSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class HomePageView(TemplateView):
    template_name = "weather_app/home.html"


class WeatherPageView(LoginRequiredMixin, ListView):
    model = Weather
    context_object_name = 'weather_data'
    template_name = "weather_app/weather.html"
    paginate_by = 3


class SuccessPageView(FormView):
    success_url = '/weather/'


class LogoutView(SuccessURLAllowedHostsMixin, TemplateView):
    next_page = None
    redirect_field_name = 'next'
    template_name = 'accounts/login.html'
    extra_context = None


class WeatherAPI(APIView):
    """
    This class serializes all the fields from the Weather class and converts it to JSON format.
    """

    @method_decorator(login_required)
    def get(self, request):
        weather_data = Weather.objects.all()
        serializer = WeatherSerializer(weather_data, many=True)
        return Response(serializer.data)
