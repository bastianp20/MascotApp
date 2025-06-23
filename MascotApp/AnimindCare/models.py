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
    contraseña = models.CharField(max_length=20, default='123')
    certificado = models.FileField(upload_to='certificados/')
    institucion = models.CharField(max_length=100, choices=instituciones)
    verificado = models.BooleanField(default=False)

# el str self, hace que en la web donde estará la base de datos de django (por ahora) hace que una vez se registre la persona aparezca en el directorio de la pagina con su nombre, apellido, rut, y estado de verificacion 

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.rut} {self.verificado}" 