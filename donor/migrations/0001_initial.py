# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Donor'
        db.create_table(u'donor_donor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('institution_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'donor', ['Donor'])

        # Adding model 'Phone'
        db.create_table(u'donor_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donor.Donor'])),
            ('preferred', self.gf('django.db.models.fields.BooleanField')()),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('type', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
        ))
        db.send_create_signal(u'donor', ['Phone'])

        # Adding model 'Address'
        db.create_table(u'donor_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donor.Donor'])),
            ('preferred', self.gf('django.db.models.fields.BooleanField')()),
            ('care_of', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('line1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('line2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'donor', ['Address'])

        # Adding model 'Donation'
        db.create_table(u'donor_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donor.Donor'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('monetary_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('in_kind', self.gf('django.db.models.fields.BooleanField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'donor', ['Donation'])

        # Adding model 'DonorContact'
        db.create_table(u'donor_donorcontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donor.Donor'])),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 20, 0, 0))),
            ('type', self.gf('django.db.models.fields.CharField')(default='P', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'donor', ['DonorContact'])


    def backwards(self, orm):
        # Deleting model 'Donor'
        db.delete_table(u'donor_donor')

        # Deleting model 'Phone'
        db.delete_table(u'donor_phone')

        # Deleting model 'Address'
        db.delete_table(u'donor_address')

        # Deleting model 'Donation'
        db.delete_table(u'donor_donation')

        # Deleting model 'DonorContact'
        db.delete_table(u'donor_donorcontact')


    models = {
        u'donor.address': {
            'Meta': {'object_name': 'Address'},
            'care_of': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donor.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'line2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'postalCode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'preferred': ('django.db.models.fields.BooleanField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'donor.donation': {
            'Meta': {'object_name': 'Donation'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donor.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_kind': ('django.db.models.fields.BooleanField', [], {}),
            'monetary_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        u'donor.donor': {
            'Meta': {'object_name': 'Donor'},
            'added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'})
        },
        u'donor.donorcontact': {
            'Meta': {'object_name': 'DonorContact'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 20, 0, 0)'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donor.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        u'donor.phone': {
            'Meta': {'object_name': 'Phone'},
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donor.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'preferred': ('django.db.models.fields.BooleanField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'})
        }
    }

    complete_apps = ['donor']