from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Увеличить количество на складе на 1")
def plus_one_quantity(modeladmin, request, queryset):
    for product in queryset:
        product.quantity += 1
        product.save()


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')
    list_filter = ('registration_date',)
    search_fields = ('name', 'email')
    search_help_text = "Поиск по имени и электронной почте"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('name',)
    search_help_text = "Поиск по названию"
    actions = [plus_one_quantity]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'product', 'quantity', 'date', 'total_sum')
    list_filter = ('date', 'client')
    search_fields = ('client__name', 'product__name')
    search_help_text = "Поиск по имени клиента или продукта"
    fieldsets = (
        (None, {
            'fields': ('client', 'product', 'quantity', 'total_sum')
        }),
        ('Дополнительно', {
            'classes': ('collapse',),
            'fields': ('date',),
        }),
    )
    readonly_fields = ('total_sum',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
