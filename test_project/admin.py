from django.contrib import admin
from .models import *

class ProjectPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1

class ProjectPhotoAdmin(admin.ModelAdmin):
    inlines = [ProjectPhotoInline]

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product, ProjectPhotoAdmin)
admin.site.register(Rating)
admin.site.register(Review)