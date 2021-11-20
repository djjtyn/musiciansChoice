# Import the depenendencies for creating forms using django
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.CharField(widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder' : 'Email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder' : 'Password'}) )

# RegistrationForm class extends djangos UserCreationForm
class RegistrationForm(forms.ModelForm):
    # Widgets allow classes to be added to the form inputs they are applied to. Using bootstrap's form-control class on all inputs
    f_name = forms.CharField(label = 'First Name')
    l_name = forms.CharField(label = 'Last Name')
    email = forms.EmailField(max_length = 40, widget = forms.EmailInput())
    password = forms.CharField(widget = forms.PasswordInput())
    passwordConfirm = forms.CharField(widget = forms.PasswordInput())
    
    # Meta class to provide the model to be used for the form
    class Meta: 
        model = CustomUser
        fields = ('f_name', 'l_name', 'email', 'password')
    
    # make sure there isn't already an existing account wit hthe asame email address
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        user_list = CustomUser.objects.filter(email=email)
        if user_list.count():
            raise ValidationError("Issue creating account")
            
    def clean_password(self):
        print(self.cleaned_data['passwordConfirm'])
        password = self.cleaned_data['password']
        passwordConfirm = self.cleaned_data['passwordConfirm']
        if password != passwordConfirm:
            raise ValidationError("Provided passwords dont match")
            
    def save(self, commit=False):
        context = {
            'f_name' : self.cleaned_data['f_name'],
            'l_name' : self.cleaned_data['l_name'],
            'email' : self.cleaned_data['email'],
            'password' : self.cleaned_data['password']
            
        }
        
        custom_user = CustomUser.objects.create_customer(context['f_name'], context['l_name'], context['email'], context['password'])

#     # Constructor for the form
#     def __init__(self, *args, **kwargs):
#         super(RegistrationForm, self).__init__(*args, **kwargs)
#         ## Loop through every input in the form and add a bootstrap 'form-control' class
#         for inputField in self.visible_fields():
#             inputField.field.widget.attrs['class'] = 'form-control'
            
# class CustomUserChangeForm(UserChangeForm):
#         class Meta:
#             model = CustomUser
#             fields = '__all__'
        


       
        