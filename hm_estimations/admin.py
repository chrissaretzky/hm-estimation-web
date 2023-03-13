from django.contrib import admin
from .models import Estimations, Images

class ImageInline(admin.TabularInline):
    model = Images

class EstimationsAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Estimations, EstimationsAdmin)