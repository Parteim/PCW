from django import forms

from .models import VkBotModel, VkCommunity


class VkBotCreationForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'id': 'bot_name',
            'class': 'bot_name_field',
            'name': 'bot_name',
            'placeholder': 'Bot name',

        }
    ))

    access_token = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'id': 'access_token',
            'class': 'access_token_field',
            'name': 'access_token',
            'placeholder': 'Access token',
        }
    ))

    class Meta:
        model = VkBotModel
        fields = ('name', 'access_token',)


class VkCommunityForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'id': 'group_name',
            'class': 'group_name_field',
            'name': 'group_name',
            'placeholder': 'Group name',

        }
    ))

    domain = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'id': 'domain',
            'class': 'domain_field',
            'name': 'domain',
            'placeholder': 'Domain',
        }
    ))

    owner_id = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'id': 'owner_id',
            'class': 'owner_id_field',
            'name': 'owner_id',
            'placeholder': 'Owner id',
        }
    ))

    class Meta:
        model = VkCommunity
        fields = ('name', 'domain', 'owner_id', )
