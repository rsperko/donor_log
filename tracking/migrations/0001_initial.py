# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entity'
        db.create_table(u'tracking_entity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('institution_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'tracking', ['Entity'])

        # Adding model 'Phone'
        db.create_table(u'tracking_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='phones', to=orm['tracking.Entity'])),
            ('primary', self.gf('django.db.models.fields.BooleanField')()),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('type', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
        ))
        db.send_create_signal(u'tracking', ['Phone'])

        # Adding model 'Address'
        db.create_table(u'tracking_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='addresses', to=orm['tracking.Entity'])),
            ('primary', self.gf('django.db.models.fields.BooleanField')()),
            ('care_of', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('line1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('line2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'tracking', ['Address'])

        # Adding model 'Communication'
        db.create_table(u'tracking_communication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracking.Entity'])),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 28, 0, 0))),
            ('type', self.gf('django.db.models.fields.CharField')(default='P', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('connected', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'tracking', ['Communication'])

        # Adding model 'ClientInformation'
        db.create_table(u'tracking_clientinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='client_information', to=orm['tracking.Entity'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='U', max_length=1)),
        ))
        db.send_create_signal(u'tracking', ['ClientInformation'])

        # Adding model 'Service'
        db.create_table(u'tracking_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='services', to=orm['tracking.ClientInformation'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('type', self.gf('django.db.models.fields.CharField')(default='H', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'tracking', ['Service'])

        # Adding model 'FamilyMember'
        db.create_table(u'tracking_familymember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='family_members', to=orm['tracking.ClientInformation'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='F', max_length=1)),
        ))
        db.send_create_signal(u'tracking', ['FamilyMember'])

        # Adding model 'DonorInformation'
        db.create_table(u'tracking_donorinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='donor_information', to=orm['tracking.Entity'])),
            ('category', self.gf('django.db.models.fields.CharField')(default='U', max_length=1)),
            ('type', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
        ))
        db.send_create_signal(u'tracking', ['DonorInformation'])

        # Adding model 'Donation'
        db.create_table(u'tracking_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='donations', to=orm['tracking.DonorInformation'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('monetary_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='H', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'tracking', ['Donation'])

        # Adding model 'VolunteerInformation'
        db.create_table(u'tracking_volunteerinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='volunteer_information', to=orm['tracking.Entity'])),
        ))
        db.send_create_signal(u'tracking', ['VolunteerInformation'])

        # Adding model 'Skill'
        db.create_table(u'tracking_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volunteer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skills', to=orm['tracking.VolunteerInformation'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='S', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'tracking', ['Skill'])


    def backwards(self, orm):
        # Deleting model 'Entity'
        db.delete_table(u'tracking_entity')

        # Deleting model 'Phone'
        db.delete_table(u'tracking_phone')

        # Deleting model 'Address'
        db.delete_table(u'tracking_address')

        # Deleting model 'Communication'
        db.delete_table(u'tracking_communication')

        # Deleting model 'ClientInformation'
        db.delete_table(u'tracking_clientinformation')

        # Deleting model 'Service'
        db.delete_table(u'tracking_service')

        # Deleting model 'FamilyMember'
        db.delete_table(u'tracking_familymember')

        # Deleting model 'DonorInformation'
        db.delete_table(u'tracking_donorinformation')

        # Deleting model 'Donation'
        db.delete_table(u'tracking_donation')

        # Deleting model 'VolunteerInformation'
        db.delete_table(u'tracking_volunteerinformation')

        # Deleting model 'Skill'
        db.delete_table(u'tracking_skill')


    models = {
        u'tracking.address': {
            'Meta': {'object_name': 'Address'},
            'care_of': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'to': u"orm['tracking.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'line2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'postalCode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'primary': ('django.db.models.fields.BooleanField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'tracking.clientinformation': {
            'Meta': {'object_name': 'ClientInformation'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'client_information'", 'to': u"orm['tracking.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'})
        },
        u'tracking.communication': {
            'Meta': {'object_name': 'Communication'},
            'connected': ('django.db.models.fields.BooleanField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 28, 0, 0)'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracking.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        u'tracking.donation': {
            'Meta': {'object_name': 'Donation'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'donations'", 'to': u"orm['tracking.DonorInformation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monetary_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'})
        },
        u'tracking.donorinformation': {
            'Meta': {'object_name': 'DonorInformation'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'donor_information'", 'to': u"orm['tracking.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'})
        },
        u'tracking.entity': {
            'Meta': {'object_name': 'Entity'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'tracking.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'family_members'", 'to': u"orm['tracking.ClientInformation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'})
        },
        u'tracking.phone': {
            'Meta': {'object_name': 'Phone'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phones'", 'to': u"orm['tracking.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'primary': ('django.db.models.fields.BooleanField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'})
        },
        u'tracking.service': {
            'Meta': {'object_name': 'Service'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['tracking.ClientInformation']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'})
        },
        u'tracking.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': u"orm['tracking.VolunteerInformation']"})
        },
        u'tracking.volunteerinformation': {
            'Meta': {'object_name': 'VolunteerInformation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'volunteer_information'", 'to': u"orm['tracking.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tracking']