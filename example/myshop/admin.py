from django.contrib import admin

from models import Category, Book, BulkDiscount


class CategoryAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


class BulkDiscountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BulkDiscount, BulkDiscountAdmin)

