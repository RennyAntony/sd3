
from django.contrib import admin
from django.urls import path as url , include
from core.views import TestView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url('admin/', admin.site.urls),
    url('',TestView.as_view() ,name="test"),
    url('api/token/',obtain_auth_token, name="obtain_token"),
    url('rest-auth/', include('rest_auth.urls')),
    url('dj-rest-auth/', include('dj_rest_auth.urls')),

]
