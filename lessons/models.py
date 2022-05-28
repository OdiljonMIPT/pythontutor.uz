from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Lesson(models.Model):
    title = models.CharField(max_length=150)
    # _______________________
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title



@receiver(pre_save, sender=Lesson)
def article_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()
