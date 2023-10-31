from django.contrib import admin
from .models import Product,Category,ProductBuy,Payment



class ProductAdmin(admin.ModelAdmin):
    list_display=["name","category","cost","date"]
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(ProductBuy)
admin.site.register(Payment)
admin.site.register(Product,ProductAdmin)
