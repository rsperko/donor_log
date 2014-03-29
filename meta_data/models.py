from django.db import models

from tracking.models import ENTITY_META_DATA, CLIENT_META_DATA, VOLUNTEER_META_DATA, DONOR_META_DATA

# Create your models here.

META_DATA = {
    'ENTITY': ENTITY_META_DATA,
    'CLIENT': CLIENT_META_DATA,
    'DONOR': DONOR_META_DATA,
    'VOLUNTEER': VOLUNTEER_META_DATA,
}