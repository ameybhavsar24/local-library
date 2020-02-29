from django.shortcuts import render
from catalog.models import Author, Genre, Book, BookInstance

# Create your views here.


def index(request):
	# Generate counts of some of the main objects
    genre_search = 'fantasy'
    num_genre = Genre.objects.filter(name__contains = genre_search).count()

    num_books = Book.objects.all().count()


    num_instances = BookInstance.objects.count()
    instance_search = 'harry'
    num_instances_searched = 0
    for x in BookInstance.objects.all():
        if instance_search in x.book.title.lower(): num_instances_searched+=1
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'genre_search' : genre_search,
        'num_genre' : num_genre,
        'instance_search': instance_search,
        'num_instances' : num_instances,
        'num_instances_searched' : num_instances_searched,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)	