from django import forms

from FinalProject.cars.models import CarCategory
from FinalProject.posts.mixins import DisabledFieldsMixin
from FinalProject.posts.models import CarPost


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = CarPost
        fields = ['title', 'content']
        labels = {
            'title': 'Title:',
            'content': 'Content:',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5,
                       'placeholder': 'Write the content about this car post here'}),
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
        fields = ['title', 'content', ]
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
            })
        }


class PostDeleteForm(DisabledFieldsMixin, PostBaseForm):
    disabled_fields = ('__all__',)


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
    category = forms.ChoiceField(
        required=False,
        choices=[('', 'All Categories')] + [(cat.id, cat.name) for cat in CarCategory.objects.all()],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
