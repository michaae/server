from django.db import models

# Create your models here.

class Producto(models.Model):
	NombreProducto = models.CharField(max_length=12)
	imagen = models.ImageField(upload_to="productos")
	
	class Meta:
		verbose_name='producto'
		verbose_name_plural='productos'

	def __str__(self):
		return '{}'.format(self.NombreProducto)