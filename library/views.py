from django.shortcuts import render
from .models import Genre, Author, Book, BookInstance
from django.shortcuts import render, get_object_or_404
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    # patys galite nustatyti šablonui kintamojo vardą
    context_object_name = 'my_book_list'
    # gauti sąrašą 3 knygų su žodžiu pavadinime 'ir'
    queryset = Book.objects.filter(title__icontains='ir')[:3]
    # šitą jau panaudojome. Neįsivaizduojate, kokį default kelią sukuria :)
    template_name = 'books/my_arbitrary_template_name_list.html'

    def get_queryset(self):
        return Book.objects.filter(title__icontains='ir')[:3]

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['duomenys'] = 'eilutė iš lempos'
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


def index(request):
    book_count = Book.objects.all().count()
    book_instance_count = BookInstance.objects.all().count()
    author_count = Author.objects.all().count()
    available_books_count = BookInstance.objects.filter(book_status__exact='a').count()

    context = {
        'books': book_count,
        'book_instances': book_instance_count,
        'authors': author_count,
        'available': available_books_count
    }

    return render(request, "index.html", context)

def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author.html', {'author': single_author})

def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    print(authors)
    return render(request, 'authors.html', context=context)

def books(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})