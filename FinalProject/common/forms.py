from django import forms

from FinalProject.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        labels = {
            'content': '',
        }

        error_messages = {

            'content': {
                'required': 'Content is required. Write it.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write your comment here...'})
