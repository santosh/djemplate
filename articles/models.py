from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default="default.jpg", blank=True)
    # author

    def __str__(self):
        return self.title

    def get_snippet(self):
        return " ".join(str(self.body).split()[:20]) + "..."