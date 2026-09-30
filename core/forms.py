from django import forms 
from core.models import UserProfile

class CustomSignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'first Name'}))
    
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'last name'})) 
    phone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'phone number'}))
    
    def signup(self, request, user):
        """called after user is created but before saved to handle additional fields""" 
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name'] 
        user.save()
    
        profile = UserProfile(user=user) 
        profile.phone = self.cleaned_data.get('phone', '')
        profile.save()
    