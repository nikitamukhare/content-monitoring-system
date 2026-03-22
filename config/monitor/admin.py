from django.contrib import admin
from .models import Keyword, ContentItem, Flag
# Register your models here.

admin.site.register(Keyword)
admin.site.register(ContentItem)
admin.site.register(Flag)