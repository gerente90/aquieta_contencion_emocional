from django.contrib import admin
from .models import Artist, Album

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass
