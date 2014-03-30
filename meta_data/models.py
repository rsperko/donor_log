from django.db import models

from tracking.models import ENTITY_META_DATA, CLIENT_META_DATA, VOLUNTEER_META_DATA, DONOR_META_DATA, COMMON_META_DATA

# Create your models here.

META_DATA = {
    'common': COMMON_META_DATA,
    'entity': ENTITY_META_DATA,
    'client': CLIENT_META_DATA,
    'donor': DONOR_META_DATA,
    'volunteer': VOLUNTEER_META_DATA,
}