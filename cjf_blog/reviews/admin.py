from django.contrib import admin

from .models import Review, Category, Subject

admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Subject)