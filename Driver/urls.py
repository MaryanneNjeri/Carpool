from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.landing,name = 'Landing'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^profile/(\d+)',views.profile,name='Profile'),
    url(r'^trip/(\d+)',views.trip,name='Trip'),
    url(r'^car/(\d+)',views.car,name='Car'),
    url(r'^passenger/(\d+)',views.passenger,name='Passenger')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
