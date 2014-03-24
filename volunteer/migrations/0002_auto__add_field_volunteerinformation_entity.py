# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'VolunteerInformation.entity'
        db.add_column(u'volunteer_volunteerinformation', 'entity',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, related_name='volunteer_information', to=orm['entity.Entity']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'VolunteerInformation.entity'
        db.delete_column(u'volunteer_volunteerinformation', 'entity_id')


    models = {
        u'entity.entity': {
            'Meta': {'object_name': 'Entity'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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
        u'volunteer.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': u"orm['volunteer.VolunteerInformation']"})
        },
        u'volunteer.volunteerinformation': {
            'Meta': {'object_name': 'VolunteerInformation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'availability': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'availability'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.Availability']"}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'volunteer_information'", 'to': u"orm['entity.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['volunteer']