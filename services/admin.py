from django.contrib import admin

# Register your models here.


from services.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("sportsman",)
    list_filter = ("sportsman",)

    # def count_favorites(self, obj):
    #     return obj.favorites.count()


admin.site.register(Subscription, SubscriptionAdmin)
