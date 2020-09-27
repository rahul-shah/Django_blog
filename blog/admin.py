from django.contrib import admin
from .models import Post,PostImage,ContactModel
from django.db import models

class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Post

 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    
    class Meta:
       model = ContactModel