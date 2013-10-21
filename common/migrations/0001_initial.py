# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Foto'
        db.create_table('common_foto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('common', ['Foto'])


    def backwards(self, orm):
        
        # Deleting model 'Foto'
        db.delete_table('common_foto')


    models = {
        'common.foto': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Foto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['common']
