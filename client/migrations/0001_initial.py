# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClientInformation'
        db.create_table(u'client_clientinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='I', max_length=1)),
        ))
        db.send_create_signal(u'client', ['ClientInformation'])

        # Adding model 'Service'
        db.create_table(u'client_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='services', to=orm['client.ClientInformation'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('type', self.gf('django.db.models.fields.CharField')(default='H', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'client', ['Service'])

        # Adding model 'FamilyMember'
        db.create_table(u'client_familymember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='family_members', to=orm['client.ClientInformation'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='F', max_length=1)),
        ))
        db.send_create_signal(u'client', ['FamilyMember'])


    def backwards(self, orm):
        # Deleting model 'ClientInformation'
        db.delete_table(u'client_clientinformation')

        # Deleting model 'Service'
        db.delete_table(u'client_service')

        # Deleting model 'FamilyMember'
        db.delete_table(u'client_familymember')


    models = {
        u'client.clientinformation': {
            'Meta': {'object_name': 'ClientInformation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1'})
        },
        u'client.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'family_members'", 'to': u"orm['client.ClientInformation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'})
        },
        u'client.service': {
            'Meta': {'object_name': 'Service'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['client.ClientInformation']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'})
        }
    }

    complete_apps = ['client']