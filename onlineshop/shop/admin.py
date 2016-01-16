from django.contrib import admin

from shop import models
# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Wishlist)
admin.site.register(models.ProductComment)
admin.site.register(models.History)
admin.site.register(models.FaultyProduct)
admin.site.register(models.CommandLine)
