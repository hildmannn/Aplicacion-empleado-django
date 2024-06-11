from django.contrib import admin
from .models import pruebaModel, departamento, addPrueba
# Register your models here.

admin.site.register(pruebaModel)



class mejorarAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name', 'shortName','cuenta',
        )
    

    def cuenta (self, obj):
        return obj.name + ' ' + obj.shortName 
        

admin.site.register(departamento, mejorarAdmin)

admin.site.register(addPrueba)