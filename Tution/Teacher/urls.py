from django.urls import path
from Teacher.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]