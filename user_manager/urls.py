from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.account, name='account'),
    url(r'^/register/$', views.RegisterFormView.as_view(), name='registration'),
    url(r'^/login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^/logout/$', views.LogoutView.as_view(), name='logout'),
]