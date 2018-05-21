from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^$',views.landing,name = 'Landing'),
    url(r'^signup/',views.signup,name='signup'),
]
