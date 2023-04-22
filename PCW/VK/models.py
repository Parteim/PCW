from django.db import models
from django.urls import reverse


class Post(models.Model):
    date = models.DateField(null=True)
    text = models.TextField(null=True)
    reposts = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    owner_id = models.IntegerField()
    from_id = models.IntegerField()
    post_id = models.IntegerField()

    def __str__(self):
        return f'db_id:{self.pk}; post_id:{self.post_id}; from_id:{self.from_id}'

    def get_absolut_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='vk')
