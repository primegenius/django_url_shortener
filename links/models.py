from django.db import models
from django.utils.text import slugify


# Create your models here.
class Links(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.slug}"
    
    def clicks(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        return super().save(*args, **kwargs)
        