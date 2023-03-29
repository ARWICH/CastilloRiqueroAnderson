from django.db import models

# Create your models here.

    
class Pais(models.Model):
        nombre = models.CharField(max_length=50,blank=False, null=False)
        nacionalidad = models.CharField(max_length=50,blank=False, null=False)   
        
        class Meta:
             verbose_name = 'Pais'
        
        def __str__(self):
         return self.nombre

class Persona(models.Model):
    id = models.IntegerField(max_length=15,blank=False, null=False,primary_key=True)
    nombre = models.CharField(max_length=35,blank=False, null=False)
    nacimiento = models.DateField()
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE)

    class  Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        
    def __str__(self):
        return self.nacionalidad.nombre