from django.db import models

# Create your models here.

class veterinarios(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    Email = models.EmailField()
    Certificado = models.FileField(upload_to='certificados/')
    verificado = models.BooleanField(default=False) 

    def __str__(self):
        return self.Nombre