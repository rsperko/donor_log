from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.decorators import login_required

admin.autodiscover()

from rest_framework import routers

from entity.views import EntityViewSet
from client.views import ClientInformationViewSet
from donor.views import DonorInformationViewSet
from meta_data.views import MetaDataViewSet
from volunteer.views import VolunteerInformationViewSet

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

    url(r'^entities/', include('entity.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^meta_data/(?P<resource_id>\d+)[/]?$', MetaDataViewSet.as_view(), name='meta_data_view'),
    url(r'^meta_data[/]?$', MetaDataViewSet.as_view(), name='meta_data_view'),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)
