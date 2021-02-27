from django.contrib import admin
from .models import *
from .export_csv import export_csv

export_csv.short_description = u"Export Artist Musics to CSV"

class ExportMusicsArtistAdmin(admin.ModelAdmin):
    actions = [export_csv]

admin.site.register(Artist, ExportMusicsArtistAdmin)
admin.site.register(Music)