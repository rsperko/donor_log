from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from entity.views import EntityViewSet
from client.views import ClientInformationViewSet
from donor.views import DonorInformationViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'entity', EntityViewSet)
router.register(r'donors', DonorInformationViewSet)
router.register(r'client', ClientInformationViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'donor_log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^entities/', include('entity.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)
