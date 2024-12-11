from django import forms

from FinalProject.cars.models import CarCategory
from FinalProject.posts.mixins import DisabledFieldsMixin
from FinalProject.posts.models import CarPost


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = CarPost
        fields = ['title', 'content', 'related_cars']
        labels = {
            'title': 'Title:',
            'content': 'Content:',
            'related_cars': 'Related Cars:'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5,
                       'placeholder': 'Write the content about this car post here'}),
            'related_cars': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),
        }
        error_messages = {
            'title': {
                'unique': "That title is already taken! Try to publish a post with a different title!",
            },
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    class Meta:
        model = CarPost
        fields = ['title', 'content', 'related_cars']
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
            }),
            'related_cars': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),
        }


class PostDeleteForm(DisabledFieldsMixin, PostBaseForm):
    disabled_fields = ('__all__',)

    class Meta(PostBaseForm.Meta):
        exclude = ('related_cars',)


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by title or content...'
        })
    )
