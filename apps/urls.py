from apps import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^categories$', views.categories, name = "home"),
]
