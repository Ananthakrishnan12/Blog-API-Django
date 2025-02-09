from django.contrib import admin
from Blogpost.models import blogpost,Comment

# Register your models here.
admin.site.register(blogpost)
admin.site.register(Comment)
