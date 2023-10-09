from django.contrib import admin

# Register your models here.


from services.models import Subscription, SubscriptionSale, Tarif, Product, ProductSale


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("sportsman", "start", "finish")
    list_filter = ("sportsman", "start", "finish")


class TarifAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "price")
    list_filter = ("name", "type", "price")

# Create your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    list_filter = ("name", "price")

class ProductSaleAdmin(admin.ModelAdmin):
    list_display = ("product", "sportsman", "trainer")
    list_filter = ("product", "sportsman", "trainer")

class SubscriptionSaleAdmin(admin.ModelAdmin):
    list_display = ("sportsman", "trainer")
    list_filter = ("sportsman", "trainer")

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSale, SubscriptionSaleAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Tarif, TarifAdmin)
admin.site.register(SubscriptionSale, SubscriptionSaleAdmin)
