from apps import views
from django.conf.urls import url

urlpatterns = [
      url(r"^$", views.homepage),
      url(r"^login$", views.login),
      url(r"^register$", views.signup),
]

