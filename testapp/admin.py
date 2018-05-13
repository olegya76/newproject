from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Dolznost)
admin.site.register(Sotrudnik)
admin.site.register(Peredacha)
admin.site.register(Reklama)
admin.site.register(Efir)
admin.site.register(Sotrudnik_in_efir)
admin.site.register(Reklama_in_efir)
