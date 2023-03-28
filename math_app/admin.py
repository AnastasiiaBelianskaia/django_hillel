from django.contrib import admin

from .models import Logs, Person


class LogsAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'path', 'method')
    list_display_links = ('user', 'timestamp')
    list_filter = ['method', 'timestamp']
    fields = ('user', ('path', 'method'), 'data')
    radio_fields = {"method": admin.VERTICAL}
    search_fields = ['timestamp', 'path', 'method']
    search_help_text = 'Search by timestamp, path or method'
    date_hierarchy = 'timestamp'


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ['last_name']
    search_fields = ['first_name', 'last_name']
    search_help_text = 'Search by first name or last name'


admin.site.register(Logs, LogsAdmin)
admin.site.register(Person, PersonAdmin)
