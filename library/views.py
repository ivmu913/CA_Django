from .models import Genre, Author, Book, BookInstance
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    book_count = Book.objects.all().count()
    book_instance_count = BookInstance.objects.all().count()
    author_count = Author.objects.all().count()
    available_books_count = BookInstance.objects.filter(book_status__exact='a').count()
    number_of_visits = request.session.get('number_of_visits', 1)
    request.session['number_of_visits'] = number_of_visits + 1

    context = {
        'books': book_count,
        'book_instances': book_instance_count,
        'authors': author_count,
        'available': available_books_count,
        'number_of_visits': number_of_visits
    }

    return render(request, "index.html", context)

def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author.html', {'author': single_author})

def authors(request):
    paginator = Paginator(Author.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)
    context = {
        'authors': paged_authors
    }
    return render(request, 'authors.html', context=context)

def books(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = 'book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Book.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    return render(request, 'search.html', {'books': search_results, 'query': query})