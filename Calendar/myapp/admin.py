from django.contrib import admin

from .models import Entry


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['author', 'name', 'date','description']
    fieldsets = [
        ('Podatki o uporabniku',               {'fields': ['author']}),
        (None,               {'fields': ['name']}),
        ('Datum', {'fields': ['date']}),
        ('Opis dogodka', {'fields': ['description']}),
    ]
admin.site.register(Entry, QuestionAdmin)


# admin.site.register(Entry)