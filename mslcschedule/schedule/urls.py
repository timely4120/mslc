from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),

    url(r'^tutor/$', views.tutor_list, name='tutor_list'),
    url(r'^tutor/(?P<pk>\d+)/delete/$', views.tutor_delete, name='tutor_delete'),
    url(r'^tutor/(?P<pk>\d+)/edit/$', views.tutor_edit, name='tutor_edit'),
    url(r'^tutor/(?P<pk>\d+)/profile/$', views.profile, name='profile'),
    url(r'^tutor/create/$', views.tutor_new, name='tutor_new'),

    url(r'^subject/$', views.subject_list, name='subject_list'),
    url(r'^subject/(?P<pk>\d+)/delete/$', views.subject_delete, name='subject_delete'),
    url(r'^subject/(?P<pk>\d+)/edit/$', views.subject_edit, name='subject_edit'),
    url(r'^subject/create/$', views.subject_new, name='subject_new'),

    url(r'^shift/$', views.shift_list, name='shift_list'),
    url(r'^shift/(?P<pk>\d+)/delete/$', views.shift_delete, name='shift_delete'),
    url(r'^shift/(?P<pk>\d+)/edit/$', views.shift_edit, name='shift_edit'),
    url(r'^shift/create/$', views.shift_new, name='shift_new'),

]
