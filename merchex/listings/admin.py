from django.contrib import admin

from listings.models import Band, Title

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed')

class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'type', 'sold')

admin.site.register(Band, BandAdmin)
admin.site.register(Title, TitleAdmin)


