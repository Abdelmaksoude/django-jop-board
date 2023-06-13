from django import forms
from .models import Apply , Jop , Comment

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','cv','cover_letter']

class JopForm(forms.ModelForm):
    class Meta:
        model = Jop
        fields = '__all__'
        exclude = ('owner','slug')

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment' , )