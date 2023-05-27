from django.db import models
from django.urls import reverse

from django.conf import settings


class VkBotModel(models.Model):
    name = models.CharField(max_length=100)
    access_token = models.TextField(null=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'bot name:{self.name}, user:{self.user}'


class VkCommunityBotModel(models.Model):
    bot_slug = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=100)
    access_token = models.TextField(null=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Post(models.Model):
    date = models.DateField(null=True)
    text = models.TextField(null=True)
    reposts = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    from_id = models.IntegerField()
    post_id = models.IntegerField()

    owner_id = models.ForeignKey('VkCommunity', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'db_id:{self.pk}; post_id:{self.post_id}; from_id:{self.from_id}'

    def get_absolut_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='vk_posts_img')


class VkCommunity(models.Model):
    name = models.CharField(max_length=150)
    domain = models.CharField(max_length=250)
    image = models.ImageField(upload_to='vk_community_img', default='vk_community_img/group.png')

    owner_id = models.IntegerField(unique=True, primary_key=True)

    parser = models.ForeignKey(VkBotModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'group_id:{self.owner_id}; name:{self.name}; domain:{self.domain}'
