# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DonorInformation'
        db.create_table(u'donor_donorinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(default='I', max_length=1)),
            ('type', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
        ))
        db.send_create_signal(u'donor', ['DonorInformation'])

        # Adding model 'Donation'
        db.create_table(u'donor_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='donations', to=orm['donor.DonorInformation'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('monetary_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='H', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'donor', ['Donation'])


    def backwards(self, orm):
        # Deleting model 'DonorInformation'
        db.delete_table(u'donor_donorinformation')

        # Deleting model 'Donation'
        db.delete_table(u'donor_donation')


    models = {
        u'donor.donation': {
            'Meta': {'object_name': 'Donation'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'donations'", 'to': u"orm['donor.DonorInformation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monetary_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'})
        },
        u'donor.donorinformation': {
            'Meta': {'object_name': 'DonorInformation'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'})
        }
    }

    complete_apps = ['donor']