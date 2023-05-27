
from django.urls import path
from .views import index, get_posts, get_bot_list, create_vk_bot, vk_bot_instance, bot_settings, add_group_to_parse_list

urlpatterns = [
    path('', index, name='home'),
    path('get_posts', get_posts, name='get-posts'),
    path('bot_list', get_bot_list, name='bot-list'),
    path('create_vk_bot', create_vk_bot, name='create-vk-bot'),
    path('bot_settings', bot_settings, name='bot-settings'),
    path('vk_bot_instance/<int:pk>', vk_bot_instance, name='vk-bot-instance'),
    path('add_vk_group/<int:bot_id>', add_group_to_parse_list, name='add-community'),
]
