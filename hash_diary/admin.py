from django.contrib import admin

from .models import Pack, Trail

class PackAdmin(admin.ModelAdmin):
	list_display = ('name', 'short_name', 'territory', 'region', 'active')
	search_fields = ['name']

admin.site.register(Pack, PackAdmin)

class TrailAdmin(admin.ModelAdmin):
	list_display = ('datetime', 'pack', 'location', 'on_down', 'hare', 'number')
	list_filter = ['datetime']
	search_field = ['location', 'on_down']

admin.site.register(Trail, TrailAdmin)

