# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    CHOICES = [('employer', 'Employer'), ('applicant', 'Applicant')]

    user_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2',"user_type"]
        
    
    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')

        if user_type not in ['employer', 'applicant']:
            raise forms.ValidationError("Invalid user type selection")
        
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''
        
    
class AccountAuthenticationForm(forms.ModelForm):
    password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = User
        fields=('username','password',)
    
    def clean(self):
        if self.is_valid():
            username=self.cleaned_data['username']
            password=self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid Credentials.")