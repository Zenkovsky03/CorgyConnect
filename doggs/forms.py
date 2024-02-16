from django.forms import ModelForm
from .models import Dog

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'