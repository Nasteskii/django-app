from django.contrib import admin
from .models import Post, EditUser, Comment


# Register your models here.

class UserAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user):
            return True
        return False


admin.site.register(EditUser, UserAdmin)


class CommentAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.commented_post.author
                    or request.user == obj.comment_author
                    or request.user.is_superuser):
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return False


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author",)
    list_filter = ("date_created",)
    search_fields = ["title", "content"]
    inlines = [CommentInline]

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
