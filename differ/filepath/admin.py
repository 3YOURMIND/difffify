from django.contrib import admin

# Register your models here.
from filepath.models import FilePath, Tag

admin.site.register(FilePath)
admin.site.register(Tag)
