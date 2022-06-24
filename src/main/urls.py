from django.contrib import admin
from django.urls import path, include
from core import AUTH_APP


urlpatterns = [
    path('admin/', admin.site.urls),
    path(AUTH_APP + '/', include('google_auth.urls'))
]
