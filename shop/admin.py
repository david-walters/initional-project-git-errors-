from django.contrib import admin
from .models import Perfume

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'price')
    search_fields = ('name',)