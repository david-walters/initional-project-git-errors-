from django.contrib import admin
from .models import Perfume

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'description', 'size', 'price')
    search_fields = ('name',)