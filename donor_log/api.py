from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from rest_framework import routers

from tracking.views import EntityViewSet, \
    ClientInformationViewSet, \
    DonorInformationViewSet, \
    VolunteerInformationViewSet
from meta_data.views import MetaDataViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'entity', EntityViewSet)
router.register(r'donors', DonorInformationViewSet)
router.register(r'client', ClientInformationViewSet)
router.register(r'volunteer', VolunteerInformationViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'donor_log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^meta_data/(?P<resource_id>\d+)[/]?$', MetaDataViewSet.as_view(), name='meta_data_view'),
    url(r'^meta_data[/]?$', MetaDataViewSet.as_view(), name='meta_data_view'),
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
)
