from django.db import models

from entity.models import META_DATA as ENTITY_META_DATA
from entity.models import META_DATA as DONOR_META_DATA
from client.models import META_DATA as CLIENT_META_DATA
from volunteer.models import META_DATA as VOLUNTEER_META_DATA

# Create your models here.

META_DATA = (
    'ENTITY', ENTITY_META_DATA,
    'CLIENT', CLIENT_META_DATA,
    'DONOR', DONOR_META_DATA,
    'VOLUNTEER', VOLUNTEER_META_DATA,
)