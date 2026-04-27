
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForms(UserCreationForm):
    class Meta:
        model = User 
        fields = ('last_name','first_name','email', 'username', 'password1', 'password2')