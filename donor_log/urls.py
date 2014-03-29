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
router.register(r'entities', EntityViewSet)
router.register(r'donors', DonorInformationViewSet)
router.register(r'clients', ClientInformationViewSet)
router.register(r'volunteers', VolunteerInformationViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'donor_log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^entities/', include('tracking.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/meta_data/(?P<resource_id>\d+)[/]?$', MetaDataViewSet.as_view(), name='meta_data_view'),
    url(r'^api/meta_data[/]?$', MetaDataViewSet.as_view(), name='meta_data_view'),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)
