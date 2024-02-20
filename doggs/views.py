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
    form = DogForm()
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dogs')
    context = {
        'form': form,
    }
    return render(request, 'doggs/dog_form.html', context)

@login_required(login_url='login')
def updateDog(request, pk):
    dogObj = Dog.objects.get(id=pk)
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
    dogObj = Dog.objects.get(id=pk)
    if request.method == 'POST':
        dogObj.delete()
        return redirect('dogs')
    context = {
        'object': dogObj
    }
    return render(request, 'doggs/delete_object.html', context)
