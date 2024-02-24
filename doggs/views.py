from django.shortcuts import render, redirect
from .models import Dog, Tag
from .forms import DogForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchDogs
def dogs(request):
    dogs, search_query = searchDogs(request)
    context = {
        'dogs_list': dogs,
        'search_query': search_query
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
