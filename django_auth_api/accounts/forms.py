from django import forms
from accounts.models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ["api_key"]