from django.db import models

# Create your models here.
instituciones = [
    ('UChile', 'Universidad de Chile'),
    ('PUC', 'Pontificia Universidad Católica de Chile'),
    ('UCMaule', 'Universidad Católica del Maule'),
    ('UAustral', 'Universidad Austral de Chile'),
    ('UdeC', 'Universidad de Concepción'),
    ('UMayor', 'Universidad Mayor'),
    ('USS', 'Universidad San Sebastián'),
    ('UDLA', 'Universidad de Las Américas'),
    ('UBO', 'Universidad Bernardo O’Higgins'),
    ('UCTemuco', 'Universidad Católica de Temuco'),
    ('USTomas', 'Universidad Santo Tomás'),
    ('UVM', 'Universidad Viña del Mar'),
    ('UNAB', 'Universidad Nacional Andrés Bello'),
    ('DuocUC', 'Duoc UC'),
    ('IPValleCentral', 'Instituto Profesional Valle Central'),
    ('IDMA', 'Centro de Formación Técnica IDMA'),
    ('UAconcagua', 'Universidad de Aconcagua'),
]

class Veterinario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    rut = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    certificado = models.FileField(upload_to='certificados/')
    institucion = models.CharField(max_length=100, choices=instituciones)
    verificado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"