# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entity'
        db.create_table(u'entity_entity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('institution_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('donor_information', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='donor_information', unique=True, null=True, to=orm['donor.DonorInformation'])),
            ('client_information', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='client_information', unique=True, null=True, to=orm['client.ClientInformation'])),
        ))
        db.send_create_signal(u'entity', ['Entity'])

        # Adding model 'Phone'
        db.create_table(u'entity_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='phones', to=orm['entity.Entity'])),
            ('primary', self.gf('django.db.models.fields.BooleanField')()),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('type', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
        ))
        db.send_create_signal(u'entity', ['Phone'])

        # Adding model 'Address'
        db.create_table(u'entity_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='addresses', to=orm['entity.Entity'])),
            ('primary', self.gf('django.db.models.fields.BooleanField')()),
            ('care_of', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('line1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('line2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'entity', ['Address'])

        # Adding model 'Contact'
        db.create_table(u'entity_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity.Entity'])),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 22, 0, 0))),
            ('type', self.gf('django.db.models.fields.CharField')(default='P', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'entity', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Entity'
        db.delete_table(u'entity_entity')

        # Deleting model 'Phone'
        db.delete_table(u'entity_phone')

        # Deleting model 'Address'
        db.delete_table(u'entity_address')

        # Deleting model 'Contact'
        db.delete_table(u'entity_contact')


    models = {
        u'client.clientinformation': {
            'Meta': {'object_name': 'ClientInformation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1'})
        },
        u'donor.donorinformation': {
            'Meta': {'object_name': 'DonorInformation'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'})
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
            'date_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 22, 0, 0)'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        u'entity.entity': {
            'Meta': {'object_name': 'Entity'},
            'added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'client_information': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'client_information'", 'unique': 'True', 'null': 'True', 'to': u"orm['client.ClientInformation']"}),
            'donor_information': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'donor_information'", 'unique': 'True', 'null': 'True', 'to': u"orm['donor.DonorInformation']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'entity.phone': {
            'Meta': {'object_name': 'Phone'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phones'", 'to': u"orm['entity.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'primary': ('django.db.models.fields.BooleanField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'})
        }
    }

    complete_apps = ['entity']