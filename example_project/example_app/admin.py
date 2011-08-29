from django.contrib import admin

from .models import Example

class ExampleAdmin(admin.ModelAdmin):
        search_fields = ['title', 'position']
        list_display = ['title', 'position', 'position_link']
        fields = ('title',)

admin.site.register(Example, ExampleAdmin)
