from django.contrib import admin
# from bangazonapi.models.product import Product
from bangazonapi.models import Product, Customer, Favorite, Order, OrderProduct, Payment, ProductCategory, ProductRating, Recommendation, Rating
"""
[summary]
"""
# Register your models here.
admin.site.register(Customer)
admin.site.register(Favorite)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductRating)
admin.site.register(Rating)
admin.site.register(Recommendation)
