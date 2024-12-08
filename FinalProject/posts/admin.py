from django.contrib import admin
from .models import CarPost


@admin.register(CarPost)
class CarPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'related_cars', 'is_published'),
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)
    filter_horizontal = ('related_cars',)

    def get_readonly_fields(self, request, obj=None):

        readonly_fields = super().get_readonly_fields(request, obj)
        if not request.user.has_perm('posts.can_publish'):
            readonly_fields += ('is_published',)
        return readonly_fields
