from django.contrib import admin
from .models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'display_genre')
    list_filter = ('title', )


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'book_status', 'due_back',)
    list_filter = ('book_status', 'due_back')
    fieldsets = (
        ('General', {'fields': ('instance_id', 'book')}),
        ('Availability', {'fields': ('book_statu', 'due_back')}),
    )
    search_fields = ('instance_id', 'book_title')




admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance, BookInstanceAdmin)