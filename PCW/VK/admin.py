from django.contrib import admin

from .models import VkBotModel, VkCommunityBotModel, VkCommunity

admin.site.register(VkBotModel)
admin.site.register(VkCommunityBotModel)
admin.site.register(VkCommunity)
