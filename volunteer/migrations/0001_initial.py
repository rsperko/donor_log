# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AvailableHours'
        db.create_table(u'volunteer_availablehours', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'volunteer', ['AvailableHours'])

        # Adding model 'Availability'
        db.create_table(u'volunteer_availability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sunday', self.gf('django.db.models.fields.related.OneToOneField')(related_name='sunday', unique=True, null=True, to=orm['volunteer.AvailableHours'])),
            ('monday', self.gf('django.db.models.fields.related.OneToOneField')(related_name='monday', unique=True, null=True, to=orm['volunteer.AvailableHours'])),
            ('tuesday', self.gf('django.db.models.fields.related.OneToOneField')(related_name='tuesday', unique=True, null=True, to=orm['volunteer.AvailableHours'])),
            ('wednesday', self.gf('django.db.models.fields.related.OneToOneField')(related_name='wednesday', unique=True, null=True, to=orm['volunteer.AvailableHours'])),
            ('thursday', self.gf('django.db.models.fields.related.OneToOneField')(related_name='thursday', unique=True, null=True, to=orm['volunteer.AvailableHours'])),
            ('friday', self.gf('django.db.models.fields.related.OneToOneField')(related_name='friday', unique=True, null=True, to=orm['volunteer.AvailableHours'])),
            ('saturday', self.gf('django.db.models.fields.related.OneToOneField')(related_name='saturday', unique=True, null=True, to=orm['volunteer.AvailableHours'])),
        ))
        db.send_create_signal(u'volunteer', ['Availability'])

        # Adding model 'VolunteerInformation'
        db.create_table(u'volunteer_volunteerinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('availability', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['volunteer.Availability'], unique=True, null=True)),
        ))
        db.send_create_signal(u'volunteer', ['VolunteerInformation'])

        # Adding model 'Skill'
        db.create_table(u'volunteer_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volunteer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skills', to=orm['volunteer.VolunteerInformation'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='S', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'volunteer', ['Skill'])


    def backwards(self, orm):
        # Deleting model 'AvailableHours'
        db.delete_table(u'volunteer_availablehours')

        # Deleting model 'Availability'
        db.delete_table(u'volunteer_availability')

        # Deleting model 'VolunteerInformation'
        db.delete_table(u'volunteer_volunteerinformation')

        # Deleting model 'Skill'
        db.delete_table(u'volunteer_skill')


    models = {
        u'volunteer.availability': {
            'Meta': {'object_name': 'Availability'},
            'friday': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'friday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'monday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'saturday': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'saturday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'sunday': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'sunday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'thursday': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'thursday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'tuesday': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'tuesday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"}),
            'wednesday': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'wednesday'", 'unique': 'True', 'null': 'True', 'to': u"orm['volunteer.AvailableHours']"})
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
            'availability': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['volunteer.Availability']", 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['volunteer']