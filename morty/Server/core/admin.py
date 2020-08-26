from django.contrib import admin

from core.models import ImageData

@admin.register(ImageData)
class ImageDataAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'filename')
