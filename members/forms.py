from django import forms
from django.forms import ModelForm
from .models import Question
from django.contrib.auth.forms import UserCreationForm ,SetPasswordForm
from django.contrib.auth.models import User

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('question_text','question_image')
        label ={ 
            'question_text': '',
            'question_image': '',
        }
        widgets = {
            'question_text':forms.TextInput(attrs={'class':'form-control'})
        }

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields = ('username','password1','password2')
    
    def __init__(self,*args,**kwargs):
        super(RegisterUserForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        field = ['new_password1','new_password2']

    def __init__(self,*args,**kwargs):
        super(ChangePasswordForm,self).__init__(*args,**kwargs)

        
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'


