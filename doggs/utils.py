from . models import Dog, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def searchDogs(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)
    dogs = Dog.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)

    )
    return dogs, search_query

def paginateDogs(request, dogs, results):
    page = request.GET.get('page') #ktora strona
    #results = 3 #ile obiektow na stronie
    paginator = Paginator(dogs, results) # wywolanie
    try:
        dogs = paginator.page(page)
    except PageNotAnInteger: #jesli np nie podamy zadnej strony albo wartosc ujemna etc
        page = 1
        dogs = paginator.page(page)
    except EmptyPage: #jesli wychodzi poza zakres stron
        page = paginator.num_pages
        dogs = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, dogs