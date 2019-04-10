from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.homepage), 
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/login/'},name = "logout"),
    url(r'^settings/$', views.setting, name = "setting"),
    url(r'^mycourses/$', views.my_course, name='my_course'),
    url(r'^course/$', views.courses_list, name = "courses"),
    url(r'^course/(?P<pk>\d+)/$', views.course_detail, name = "course-detail"),
    url(r'^course/(?P<pk>\d+)/enroll/$', views.course_detail_enroll, name="course-enroll"),
    url(r'^course/(?P<pk>\d+)/enroll/learn/$', views.course_learn, name="courses-learn"),    
    url(r'^course/categories/(?P<pk>\d+)/$', views.categories, name = "categories"),
]
