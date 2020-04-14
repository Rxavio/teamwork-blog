from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('title','date_posted','date_updated','author','status')
    list_filter=('status','date_posted','date_updated')
    search_fields=('title',)
    list_editable=('status',)


admin.site.register(Post,PostAdmin)