# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Entity.donor_information'
        db.delete_column(u'entity_entity', 'donor_information_id')


    def backwards(self, orm):
        # Adding field 'Entity.donor_information'
        db.add_column(u'entity_entity', 'donor_information',
                      self.gf('django.db.models.fields.related.OneToOneField')(related_name='donor_information', unique=True, null=True, to=orm['donor.DonorInformation'], blank=True),
                      keep_default=False)


    models = {
        u'client.clientinformation': {
            'Meta': {'object_name': 'ClientInformation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1'})
        },
        u'entity.address': {
            'Meta': {'object_name': 'Address'},
            'care_of': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'to': u"orm['entity.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'line2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postalCode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'primary': ('django.db.models.fields.BooleanField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'entity.contact': {
            'Meta': {'object_name': 'Contact'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 23, 0, 0)'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        u'entity.entity': {
            'Meta': {'object_name': 'Entity'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'client_information': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'client_information'", 'unique': 'True', 'null': 'True', 'to': u"orm['client.ClientInformation']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_information': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'volunteer_information'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.VolunteerInformation']"})
        },
        u'entity.phone': {
            'Meta': {'object_name': 'Phone'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phones'", 'to': u"orm['entity.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'primary': ('django.db.models.fields.BooleanField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'})
        },
        u'volunteer.availability': {
            'Meta': {'object_name': 'Availability'},
            'friday': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'friday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'monday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'saturday': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'saturday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'sunday': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'sunday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'thursday': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'thursday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'tuesday': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'tuesday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'wednesday': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'wednesday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"})
        },
        u'volunteer.availablehours': {
            'Meta': {'object_name': 'AvailableHours'},
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'volunteer.volunteerinformation': {
            'Meta': {'object_name': 'VolunteerInformation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'availability': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'availability'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.Availability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['entity']