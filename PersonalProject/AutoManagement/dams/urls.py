from django.conf.urls import url
from dams import views

urlpatterns = [
    url(r'^login$', views.login),
]
