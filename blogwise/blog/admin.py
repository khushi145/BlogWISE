from django.contrib import admin
from .models import Post,Category,Profile

class CategoryAdmin(admin.ModelAdmin):
    list_display=('img_tag','name','description',)
    search_fields=('name',)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','category','post_date',)
    search_fields=('title',)
    list_filter=('category',)

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Profile)
