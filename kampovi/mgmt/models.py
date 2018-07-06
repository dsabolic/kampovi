from django.db import models


class Radionica(models.Model):
	name = models.CharField(
		max_length = 200
	)

	leader_name = models.CharField(
		max_length = 200
	)

	description = models.CharField(
		max_length = 200
	)

	kamp = models.ForeignKey(
		'Kamp',
		on_delete = models.CASCADE
	)

	class Meta:
		verbose_name_plural = 'Radionice'

	def __str__(self):
		return self.name


class Kamp(models.Model):
	name = models.CharField(
		max_length=150
	)

	def __str__(self):
		return self.name

	start_date = models.DateTimeField(
		'Pocetak kampa'
	)
	end_date = models.DateTimeField(
		'Kraj kampa'
	)

	class Meta:
		verbose_name_plural = 'Kampovi'
