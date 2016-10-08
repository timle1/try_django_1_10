from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "last_updated", "init_timestamp"]
    list_display_links = ["last_updated"]
    list_editable = ["title"]
    list_filter = ["last_updated", "init_timestamp"]

    search_fields = ["title", "content"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)