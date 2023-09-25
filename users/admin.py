from django.contrib import admin

# Register your models here.


from .models import Group, GroupMember, User
class UserAdmin(admin.ModelAdmin):
    list_display = ("username","email")
    list_filter = ("username","email")

class GroupAdmin(admin.ModelAdmin):
    list_display = ("groupname","trainer")
    list_filter = ("groupname","trainer")

    # def count_favorites(self, obj):
    #     return obj.favorites.count()

class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ("group","sportsman")
    list_filter = ("group","sportsman")

admin.site.register(GroupMember, GroupMemberAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)