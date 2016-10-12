from django.db import models
from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    return '{id}/{file}'.format(id=instance.id, file=filename)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    init_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'id': self.id})

    class Meta:
        ordering = ["-init_timestamp", "-last_updated"]