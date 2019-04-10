from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^categories$', views.categories, name = "categories"),
]
