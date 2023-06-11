from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Post(models.Model):
    """ Post written by user """
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="author_post")
    publish_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    excerpt = models.TextField(blank=True, default='', max_length=100)

    class Meta:
        """ Data should order by update date """
        ordering = ['-updated_on']

    def __str__(self):
        return f"{self.title} on {self.publish_on}"


@receiver(pre_save, sender=Post)
def post_pre_save(sender, instance, *args, **kwargs):
    """ auto add slug to the slug column """
    if not instance.slug:
        instance.slug = slugify(instance.title)