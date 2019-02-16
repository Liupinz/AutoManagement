from django.conf.urls import url
from dams import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logincheck$', views.logincheck),
]
