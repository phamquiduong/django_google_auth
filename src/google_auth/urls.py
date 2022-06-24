from django.urls import path
from .views import *
from core import CALL_BACK_URI

urlpatterns = [
    path('auth', authorization_url, name='authorization_url'),
    path(CALL_BACK_URI, credentials, name='credentials')
]
