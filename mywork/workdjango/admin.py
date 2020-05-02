from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post

admin.site.site_header='Admin CMS Panel'

class PostAdmin(admin.ModelAdmin):
    list_display=('title','date_posted','date_updated','author','status')
    list_filter=('status','date_posted','date_updated')
    search_fields=('title',)
    list_editable=('status',)


admin.site.register(Post,PostAdmin)
# admin.site.unregister(Group)