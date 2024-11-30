from django.contrib import admin
from .models import Car, CarCategory, TestDriveBooking


@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'category', 'price', 'available_for_test_drive')
    list_filter = ('category', 'available_for_test_drive')
    search_fields = ('brand', 'description')
    ordering = ('brand',)
    readonly_fields = ('available_for_test_drive',)

    class TestDriveBookingInline(admin.TabularInline):
        model = TestDriveBooking
        extra = 0
        fields = ('user', 'date', 'time', 'status', 'created_at')
        readonly_fields = ('created_at',)

    inlines = [TestDriveBookingInline]


@admin.register(TestDriveBooking)
class TestDriveBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'date', 'time', 'status', 'created_at')
    list_filter = ('status', 'car', 'date')
    search_fields = ('user__username', 'car__brand')
    ordering = ('-created_at',)
    date_hierarchy = 'date'
    list_editable = ('status',)
    readonly_fields = ('created_at',)
