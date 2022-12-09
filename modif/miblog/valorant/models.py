
from django.db import models
from django.core.paginator import Paginator

from django.utils.timezone import now
#from django.contrib.auth.models import User

class Categoria(models.Model):
    name=models.CharField(primary_key=True,max_length=100,verbose_name="Nombre")
    descr=models.CharField(max_length=100,verbose_name="Descripción")
    created=models.DateTimeField(auto_now_add=True,verbose_name="F. Agreg")
    updated=models.DateTimeField(auto_now_add=True,verbose_name="F. Actz")

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Role"

class Agentes(models.Model):
    title=models.CharField(max_length=100,verbose_name="Nombre Agente")
    detail=models.TextField(verbose_name="Descripción")
    image=models.ImageField(upload_to="projects")
    published=models.DateTimeField(default=now,verbose_name="F.Public")
    
    categor=models.ManyToManyField(Categoria,verbose_name="rol")
    Categoria.published=models.ForeignKey('Categoria',on_delete=models.CASCADE,verbose_name="ROL")
    


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Agente"


class formBD(models.Model):
    nombre=models.CharField(max_length=30)
    correo=models.EmailField()
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name="Registro"





