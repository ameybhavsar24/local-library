from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance


# admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
admin.site.register(Book,BookAdmin)


# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

# admin.site.register(BookInstance)

class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('due_back', 'status')
	list_filter = ('status', 'due_back')
admin.site.register(BookInstance, BookInstanceAdmin)