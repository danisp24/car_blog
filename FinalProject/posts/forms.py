from django import forms

from FinalProject.posts.models import CarPost


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = CarPost
        fields = ['title', 'content']  # Only include fields to be shown to the user
        labels = {
            'title': 'Title:',
            'content': 'Content:',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write the content about this car post here'}),
        }
        error_messages = {
            'title': {
                'unique': "That title is already taken! Try to publish a post with a different title!",
            },
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Exclude fields from user input, but still set programmatically
    #     self.fields['is_published'].widget = forms.HiddenInput()
    #     self.fields['author'].widget = forms.HiddenInput()


class PostCreateForm(PostBaseForm):
    pass



# class PostEditForm(PostBaseForm):
#     class Meta(PostBaseForm.Meta):
#         help_texts = {
#             'image_url': ''
#         }


# class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
#     read_only_fields = ['title', 'content', 'image_url']
#
#     class Meta(PostEditForm.Meta):
#         pass
