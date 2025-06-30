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


veterinario_tipo = [
    ('IND', 'Independiente'),
    ('CLIN', 'Centro veterinario'),
]

class registrar_veterinario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    rut = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=20, default='123')
    certificado = models.FileField(upload_to='certificados/')
    institucion = models.CharField(max_length=100, choices=instituciones)
    veterinario_tipo = models.CharField(max_length=4, choices=[('IND', 'Independiente'), ('CLIN', 'Centro veterinario')], default='IND')
    nombre_centro = models.CharField(max_length=200, blank=True, null=True)
    verificado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.get_veterinario_tipo_display()})"

    

class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='miembros_fotos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"