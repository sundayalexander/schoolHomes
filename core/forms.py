from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['date_joined', 'groups', 'user_permissions', 'is_staff', 'is_superuser', 'last_login']
