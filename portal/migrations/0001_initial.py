# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Telefono'
        db.create_table('portal_telefono', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('portal', ['Telefono'])

        # Adding model 'RepresentanteEmpresa'
        db.create_table('portal_representanteempresa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('cargo_es', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('cargo_en', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('portal', ['RepresentanteEmpresa'])

        # Adding model 'Empresa'
        db.create_table('portal_empresa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebook_account', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('twitter_account', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('google_account', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mision', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mision_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mision_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vision', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vision_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vision_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valores', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valores_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valores_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('historia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('historia_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('historia_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('filosofia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('filosofia_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('filosofia_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.Telefono'], null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('portal', ['Empresa'])

        # Adding model 'RepresentanteUnidad'
        db.create_table('portal_representanteunidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('portal', ['RepresentanteUnidad'])

        # Adding model 'UnidadNegocio'
        db.create_table('portal_unidadnegocio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('representante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.RepresentanteUnidad'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.Empresa'])),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('logo_inactivo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('background', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('clientes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('clientes_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('clientes_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('portal', ['UnidadNegocio'])

        # Adding model 'Categoria'
        db.create_table('portal_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('unidad_negocio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.UnidadNegocio'])),
        ))
        db.send_create_signal('portal', ['Categoria'])

        # Adding model 'CategoriaLinea'
        db.create_table('portal_categorialinea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('unidad_negocio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.UnidadNegocio'])),
        ))
        db.send_create_signal('portal', ['CategoriaLinea'])

        # Adding model 'CategoriaMarca'
        db.create_table('portal_categoriamarca', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('unidad_negocio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.UnidadNegocio'])),
        ))
        db.send_create_signal('portal', ['CategoriaMarca'])

        # Adding model 'Proyecto'
        db.create_table('portal_proyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.Categoria'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('portal', ['Proyecto'])

        # Adding M2M table for field fotos on 'Proyecto'
        db.create_table('portal_proyecto_fotos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm['portal.proyecto'], null=False)),
            ('foto', models.ForeignKey(orm['common.foto'], null=False))
        ))
        db.create_unique('portal_proyecto_fotos', ['proyecto_id', 'foto_id'])

        # Adding model 'Linea'
        db.create_table('portal_linea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('categoria_linea', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.CategoriaLinea'])),
        ))
        db.send_create_signal('portal', ['Linea'])

        # Adding model 'Marca'
        db.create_table('portal_marca', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('categoria_marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portal.CategoriaMarca'])),
        ))
        db.send_create_signal('portal', ['Marca'])

        # Adding model 'Noticia'
        db.create_table('portal_noticia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('portal', ['Noticia'])

        # Adding model 'ResponsabilidadSocial'
        db.create_table('portal_responsabilidadsocial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('introduccion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('introduccion_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('introduccion_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('politica', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('politica_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('politica_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('portal', ['ResponsabilidadSocial'])

        # Adding model 'Actividad'
        db.create_table('portal_actividad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('nombre_es', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('nombre_en', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_es', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('portal', ['Actividad'])

        # Adding M2M table for field fotos on 'Actividad'
        db.create_table('portal_actividad_fotos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actividad', models.ForeignKey(orm['portal.actividad'], null=False)),
            ('foto', models.ForeignKey(orm['common.foto'], null=False))
        ))
        db.create_unique('portal_actividad_fotos', ['actividad_id', 'foto_id'])

        # Adding model 'Contacto'
        db.create_table('portal_contacto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('portal', ['Contacto'])


    def backwards(self, orm):
        
        # Deleting model 'Telefono'
        db.delete_table('portal_telefono')

        # Deleting model 'RepresentanteEmpresa'
        db.delete_table('portal_representanteempresa')

        # Deleting model 'Empresa'
        db.delete_table('portal_empresa')

        # Deleting model 'RepresentanteUnidad'
        db.delete_table('portal_representanteunidad')

        # Deleting model 'UnidadNegocio'
        db.delete_table('portal_unidadnegocio')

        # Deleting model 'Categoria'
        db.delete_table('portal_categoria')

        # Deleting model 'CategoriaLinea'
        db.delete_table('portal_categorialinea')

        # Deleting model 'CategoriaMarca'
        db.delete_table('portal_categoriamarca')

        # Deleting model 'Proyecto'
        db.delete_table('portal_proyecto')

        # Removing M2M table for field fotos on 'Proyecto'
        db.delete_table('portal_proyecto_fotos')

        # Deleting model 'Linea'
        db.delete_table('portal_linea')

        # Deleting model 'Marca'
        db.delete_table('portal_marca')

        # Deleting model 'Noticia'
        db.delete_table('portal_noticia')

        # Deleting model 'ResponsabilidadSocial'
        db.delete_table('portal_responsabilidadsocial')

        # Deleting model 'Actividad'
        db.delete_table('portal_actividad')

        # Removing M2M table for field fotos on 'Actividad'
        db.delete_table('portal_actividad_fotos')

        # Deleting model 'Contacto'
        db.delete_table('portal_contacto')


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
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'clientes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'clientes_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'clientes_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.Empresa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo_inactivo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'nombre_es': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'representante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portal.RepresentanteUnidad']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portal']
