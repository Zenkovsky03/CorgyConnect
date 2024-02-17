from django.forms import ModelForm
from .models import Dog

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['name','description','wiki_link','tags', 'featured_image']