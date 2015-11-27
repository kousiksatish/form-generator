from django.db import models

# Create your models here.

class Forms(models.Model):
	id = models.AutoField(primary_key=True)
	uniq_url = models.CharField(max_length=200)
	title = models.CharField(max_length=400)
	description = models.CharField(max_length=1500)
	created_at = models.DateTimeField(auto_now=True)

class field_types(models.Model):
	ty_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	open_tag = models.CharField(max_length=100)
	options = models.CharField(max_length=100)
	close_tag = models.CharField(max_length=100, default='nill')
	active = models.IntegerField(default = 1)

class fields(models.Model):
	fd_id = models.AutoField(primary_key=True)
	fm_id = models.ForeignKey(Forms)
	position = models.IntegerField()
	label = models.CharField(max_length=300)
	ty_id = models.ForeignKey(field_types)
	options = models.CharField(max_length=500)

