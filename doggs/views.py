from django.shortcuts import render, redirect
from .models import Dog
from .forms import DogForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# dziala
def dogs(request):
    dogs = Dog.objects.all()
    context = {
        'dogs_list': dogs,
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
