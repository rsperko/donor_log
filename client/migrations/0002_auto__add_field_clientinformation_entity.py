# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ClientInformation.entity'
        db.add_column(u'client_clientinformation', 'entity',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='client_information', to=orm['entity.Entity']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ClientInformation.entity'
        db.delete_column(u'client_clientinformation', 'entity_id')


    models = {
        u'client.clientinformation': {
            'Meta': {'object_name': 'ClientInformation'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'client_information'", 'to': u"orm['entity.Entity']"}),
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
        },
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
        }
    }

    complete_apps = ['client']