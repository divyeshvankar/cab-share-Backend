from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','phone','pickup','drop','cab_type','trip_type')
    list_filter = ('pickup','drop','cab_type','trip_type')
    search_fields = ['name', 'phone']
    ordering = ('cab_type',)

    class Meta:
        model = Book
        fields = '__all__'