from django.core.validators import MinValueValidator
from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=50, primary_key=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    #не создавать продукт, если цена меньше 0
    # def save(self, *args, **kwargs):
    #     if self.price < 0:
    #         return
    #     super().save(*args, **kwargs)

# class Service(models.Model):
#     ...
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
#
# category1 = Category('Смартфоны', 'smartphones')
# category2 = Category('Ноутбуки', 'notebooks')
#
# prod1 = Product('Apple Iphone', ..., category1)
# prod2 = Product('Xiaomi Mi 11', ..., category1)
# prod3 = Product('Acer Aspire', ..., category2)
#
# category1.products.all()
# category1.product_set.all() #[prod1, prod2]


class Order(models.Model):
    address = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='orders', through='OrderItems')

    def __str__(self):
        return f'Заказ №: {self.id}'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = ['order', 'product']
