from django.contrib import admin
from .models import Category, Product, Address, CartItem, Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(CartItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')