from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

from rest_framework import routers

from tracking.views import EntityViewSet, \
    CommunicationViewSet
from meta_data.views import MetaDataViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'entities', EntityViewSet)
router.register(r'communications', CommunicationViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'donor_log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Login / logout.
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),

    (r'^tracking/', TemplateView.as_view(template_name = 'tracking/index.html')),

    # url(r'^entities/', include('tracking.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/meta_data/(?P<resource_id>\d+)[/]?$', MetaDataViewSet.as_view(), name='meta_data_view'),
    url(r'^api/meta_data[/]?$', MetaDataViewSet.as_view(), name='meta_data_view'),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)
