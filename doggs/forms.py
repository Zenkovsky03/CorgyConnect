from django.forms import ModelForm
from .models import Dog, Review
from django import forms

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'description', 'wiki_link', 'tags', 'featured_image']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
    def __init__(self, *args, **kwargs):
        super(DogForm, self).__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({'class': 'input', 'placeholder': 'Add name'})
        for name, field in self.fields.items():
            # if name == "description":
            field.widget.attrs.update({'class': 'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote',

        }
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({'class': 'input', 'placeholder': 'Add name'})
        for name, field in self.fields.items():
            # if name == "description":
            field.widget.attrs.update({'class': 'input'})