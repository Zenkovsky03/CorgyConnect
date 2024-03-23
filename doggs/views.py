from django.shortcuts import render, redirect
from .models import Dog, Tag
from .forms import DogForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .utils import searchDogs, paginateDogs
def dogs(request):
    dogs, search_query = searchDogs(request)
    custom_range, dogs = paginateDogs(request, dogs, 3)
    context = {
        'dogs_list': dogs,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'doggs/dogs.html', context)


def dog(request, pk):
    dogObj = Dog.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.dog = dogObj
            review.owner = request.user.profile
            review.save()

            dogObj.getVoteCount
            messages.success(request, 'Your review was successfully submitted.')
            return redirect('dog', pk=dogObj.id)
    context = {
        'dogObj': dogObj,
        'form': form,
    }
    return render(request, 'doggs/single-dog.html', context)

@login_required(login_url='login')
def createDog(request):
    profile = request.user.profile
    form = DogForm()
    if request.method == 'POST':
        newTags = request.POST.get('newTags').replace(",", " ").split()
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = profile
            dog.save()
            for tag in newTags:
                tag, created = Tag.objects.get_or_create(name=tag)
                dog.tags.add(tag)
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
        newTags = request.POST.get('newTags').replace(",", " ").split()
        form = DogForm(request.POST, request.FILES, instance=dogObj)
        if form.is_valid():
            dog = form.save()
            for tag in newTags:
                tag, created = Tag.objects.get_or_create(name=tag)
                dog.tags.add(tag)
            return redirect('dogs')
    context = {
        'form': form,
        'dogObj': dogObj,
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
