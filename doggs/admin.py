from django.contrib import admin
from .models import Dog, Review, Tag

# Register your models here.

admin.site.register(Dog)
admin.site.register(Review)
admin.site.register(Tag)
