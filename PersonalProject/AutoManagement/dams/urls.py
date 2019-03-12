from django.conf.urls import url
from dams import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logincheck$', views.logincheck),
    url(r'^mysqlsingle', views.mysqlsingle),
    url(r'^mchoice', views.mchoice),
    url(r'^singleinstall', views.singleinstall),
    url(r'^galeracluster', views.galeracluster),
    url(r'^galerainstall', views.galerainstall),
]
