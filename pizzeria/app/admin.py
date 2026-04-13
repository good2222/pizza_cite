from django.contrib import admin
from .models import Category, Pizza, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_medium', 'is_available', 'is_spicy', 'is_vegetarian']
    list_filter = ['category', 'is_available', 'is_spicy', 'is_vegetarian']
    list_editable = ['is_available']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'delivery_type']
    list_editable = ['status']
    inlines = [OrderItemInline]
