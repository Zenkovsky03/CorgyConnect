from django.shortcuts import render
from .models import Dog
from .forms import DogForm
# Create your views here.
#dziala
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

def createDog(request):
    form = DogForm()
    context = {
        'form': form,
    }
    return render(request, 'doggs/dog_form.html', context)