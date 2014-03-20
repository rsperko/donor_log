# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Donor.category'
        db.add_column(u'donor_donor', 'category',
                      self.gf('django.db.models.fields.CharField')(default='I', max_length=1),
                      keep_default=False)

        # Adding field 'Donation.type'
        db.add_column(u'donor_donation', 'type',
                      self.gf('django.db.models.fields.CharField')(default='H', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Donor.category'
        db.delete_column(u'donor_donor', 'category')

        # Deleting field 'Donation.type'
        db.delete_column(u'donor_donation', 'type')


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
            'notes': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'})
        },
        u'donor.donor': {
            'Meta': {'object_name': 'Donor'},
            'added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1'}),
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