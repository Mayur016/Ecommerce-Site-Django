from django.contrib import admin
from shop.models import Product, Order
# Register your models here.
admin.site.site_header = "Ecommerce Site"
admin.site.site_title = "Mayur Shopping"
admin.site.index_title = "Welcome to Mayur Shopping"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')

    list_display = ['title', 'price', 'discount_price', 'category', 'description', 'image']
    search_fields = ('title', 'category')
    actions = ('change_category_to_default')
    list_editable = ('price', 'discount_price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
