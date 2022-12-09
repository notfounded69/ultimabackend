from django.contrib import admin
from .models import Categoria, Agentes,formBD

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Agentes)

class paginacion(admin.ModelAdmin):
    list_per_page = 5 # la lista de resultado sera maximo de 5 y seguira en las otras paginas
    list_display = ('nombre', 'correo') #muestra el nombre y correo en el panel de administracion
admin.site.register(formBD,paginacion)


