from django.contrib import admin
from .models import  Slider, Tag, PostItem
# Register your models here.

class AdminPostItem(admin.ModelAdmin):
    fields = ['slider','title', 'author', 'body', 'picture' , 'thumbnail', 'publishable', 'description', 'tags', 'post_type', 'color' ]
    list_display = ['title', 'slider', 'author', 'publishable', 'slug','date_as_day', 'post_type']

    class Meta:
        model = PostItem

admin.site.register(Slider)
admin.site.register(Tag)
admin.site.register(PostItem, AdminPostItem)





