from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=150, min_length=1)
    description = forms.CharField()
    author = forms.IntegerField()

