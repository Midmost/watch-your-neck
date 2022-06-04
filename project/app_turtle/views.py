from re import template
from django.shortcuts import render
from django.conf.urls import include
from django.urls import reverse_lazy
from django.http import HttpResponse

from . import app_settings

def view_turtle(request):
    return render(request, "app_turtle/checkpose.html")

# PWA
# def service_worker(request):
#     response = HttpResponse(open(app_settings.PWA_SERVICE_WORKER_PATH).read(), content_type='application/javascript')
#     return response

# def manifest(request):
#     return render(request, 'manifest.json', {
#         setting_name: getattr(app_settings, setting_name)
#         for setting_name in dir(app_settings)
#         if setting_name.startswith('PWA_')
#     })