# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'UnidadNegocio.representante'
        db.delete_column('portal_unidadnegocio', 'representante_id')

        # Adding M2M table for field representantes on 'UnidadNegocio'
        db.create_table('portal_unidadnegocio_representantes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unidadnegocio', models.ForeignKey(orm['portal.unidadnegocio'], null=False)),
            ('representanteunidad', models.ForeignKey(orm['portal.representanteunidad'], null=False))
        ))
        db.create_unique('portal_unidadnegocio_representantes', ['unidadnegocio_id', 'representanteunidad_id'])


    def backwards(self, orm):
        
        # Adding field 'UnidadNegocio.representante'
        db.add_column('portal_unidadnegocio', 'representante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.RepresentanteUnidad'], null=True, blank=True), keep_default=False)

        # Removing M2M table for field representantes on 'UnidadNegocio'
        db.delete_table('portal_unidadnegocio_representantes')


    models = {
        'common.foto': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Foto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'portal.actividad': {
            'Meta': {'object_name': 'Actividad'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fotos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['common.Foto']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'})
        },
        'portal.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'unidad_negocio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.UnidadNegocio']"})
        },
        'portal.categorialinea': {
            'Meta': {'object_name': 'CategoriaLinea'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'unidad_negocio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.UnidadNegocio']"})
        },
        'portal.categoriamarca': {
            'Meta': {'object_name': 'CategoriaMarca'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'unidad_negocio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.UnidadNegocio']"})
        },
        'portal.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'portal.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facebook_account': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'filosofia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'filosofia_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'filosofia_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'google_account': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'historia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'historia_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'historia_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mision': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mision_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mision_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.Telefono']", 'null': 'True', 'blank': 'True'}),
            'twitter_account': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'valores': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'valores_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'valores_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'vision': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'vision_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'vision_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'portal.linea': {
            'Meta': {'object_name': 'Linea'},
            'categoria_linea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.CategoriaLinea']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        'portal.marca': {
            'Meta': {'object_name': 'Marca'},
            'categoria_marca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.CategoriaMarca']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'portal.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'})
        },
        'portal.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.Categoria']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fotos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['common.Foto']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'portal.representanteempresa': {
            'Meta': {'object_name': 'RepresentanteEmpresa'},
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'cargo_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'cargo_es': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portal.representanteunidad': {
            'Meta': {'object_name': 'RepresentanteUnidad'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portal.responsabilidadsocial': {
            'Meta': {'object_name': 'ResponsabilidadSocial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'introduccion_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'introduccion_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'politica': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'politica_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'politica_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'portal.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'portal.unidadnegocio': {
            'Meta': {'ordering': "('id',)", 'object_name': 'UnidadNegocio'},
            'bg_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'clientes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'clientes_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'clientes_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.Empresa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'representantes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['portal.RepresentanteUnidad']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portal']
