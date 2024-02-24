from django.shortcuts import render, redirect
from .models import Dog, Tag
from .forms import DogForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .utils import searchDogs
def dogs(request):
    dogs, search_query = searchDogs(request)

    page = request.GET.get('page') #ktora strona
    results = 3 #ile obiektow na stronie
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
    context = {
        'dogs_list': dogs,
        'search_query': search_query,
        'paginator': paginator,
        'custom_range': custom_range,
    }
    return render(request, 'doggs/dogs.html', context)


def dog(request, pk):
    dogObj = Dog.objects.get(id=pk)
    context = {
        'dogObj': dogObj
    }
    return render(request, 'doggs/single-dog.html', context)

@login_required(login_url='login')
def createDog(request):
    profile = request.user.profile
    form = DogForm()
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = profile
            dog.save()
            return redirect('account')
    context = {
        'form': form,
    }
    return render(request, 'doggs/dog_form.html', context)

@login_required(login_url='login')
def updateDog(request, pk):
    profile = request.user.profile
    dogObj = profile.dog_set.get(id=pk)
    form = DogForm(instance=dogObj)
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dogObj)
        if form.is_valid():
            form.save()
            return redirect('dogs')
    context = {
        'form': form,
    }
    return render(request, 'doggs/dog_form.html', context)

@login_required(login_url='login')
def deleteDog(request, pk):
    profile = request.user.profile
    dogObj = profile.dog_set.get(id=pk)
    if request.method == 'POST':
        dogObj.delete()
        return redirect('account')
    context = {
        'object': dogObj
    }
    return render(request, 'delete_object.html', context)
