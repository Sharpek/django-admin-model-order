from django.contrib import admin

from .models import Example

class ExampleAdmin(admin.ModelAdmin):
        search_fields = ['title', 'position']
        list_display = ['title', 'position_link']

admin.site.register(Example, ExampleAdmin)
