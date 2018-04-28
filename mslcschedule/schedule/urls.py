from django.conf.urls import url
from . import views

urlpatterns = [
    # urls for the home page
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),

    # urls having to do with tutor record
    url(r'^tutor/$', views.tutor_list, name='tutor_list'),
    url(r'^tutor/(?P<pk>\d+)/delete/$', views.tutor_delete, name='tutor_delete'),
    url(r'^tutor/(?P<pk>\d+)/edit/$', views.tutor_edit, name='tutor_edit'),
    url(r'^tutor/(?P<pk>\d+)/profile/$', views.profile, name='profile'),
    url(r'^tutor/create/$', views.tutor_new, name='tutor_new'),

    # urls having to do with subject records
    url(r'^subject/$', views.subject_list, name='subject_list'),
    url(r'^subject/(?P<pk>\d+)/delete/$', views.subject_delete, name='subject_delete'),
    url(r'^subject/(?P<pk>\d+)/edit/$', views.subject_edit, name='subject_edit'),
    url(r'^subject/create/$', views.subject_new, name='subject_new'),

    # urls having to do with shift records
    url(r'^shift/$', views.shift_list, name='shift_list'),
    url(r'^shift/(?P<pk>\d+)/delete/$', views.shift_delete, name='shift_delete'),
    url(r'^shift/(?P<pk>\d+)/edit/$', views.shift_edit, name='shift_edit'),
    url(r'^shift/create/$', views.shift_new, name='shift_new'),

    # urls having to do with availability records
    url(r'^availability/$', views.availability_list, name='availability_list'),
    url(r'^availability/(?P<pk>\d+)/delete/$', views.availability_delete, name='availability_delete'),
    url(r'^availability/(?P<pk>\d+)/edit/$', views.availability_edit, name='availability_edit'),
    url(r'^availability/create/$', views.availability_new, name='availability_new'),

    # urls having to do with course records
    url(r'^course/$', views.course_list, name='course_list'),
    url(r'^course/(?P<pk>\d+)/delete/$', views.course_delete, name='course_delete'),
    url(r'^course/(?P<pk>\d+)/edit/$', views.course_edit, name='course_edit'),
    url(r'^course/create/$', views.course_new, name='course_new'),
]
