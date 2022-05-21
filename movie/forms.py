from django import forms
from django.utils.translation import gettext_lazy as _
from django_comments_xtd.forms import XtdCommentForm
from movie.models import Comment


class MyCommentForm(XtdCommentForm):
    title = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={'placeholder': _('title')})
    )

    def get_comment_create_data(self):
        data = super(MyCommentForm, self).get_comment_create_data()
        data.update({'title': self.cleaned_data['title']})
        return data


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs=
    {
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ..',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)


