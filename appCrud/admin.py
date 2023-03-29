from django.contrib import admin

# Register your models here.
from .models import Persona, Pais

admin.site.register(Persona)
admin.site.register(Pais)