from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserCreationCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username')
