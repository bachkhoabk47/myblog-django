from django.contrib import admin
from . import models
from django.db.models import TextField


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created", "modified", "publish", "id_sort")
    list_editable = ('publish', 'id_sort' )
    search_fields = ("title", "created", "modified")
    list_filter = ('created', 'publish',)
    date_hierarchy = 'created'
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Album)
