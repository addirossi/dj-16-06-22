from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Product, Order, OrderItems
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']


class OrderItemsInlineFormset(BaseInlineFormSet):
    def clean(self):
        products_ids = set([form.cleaned_data['product'].id for form in self.forms])
        if products_ids != len(self.forms):
            raise ValidationError('Позиции дублируются')
        return super().clean()


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0
    # formset = OrderItemsInlineFormset


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline, ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems)