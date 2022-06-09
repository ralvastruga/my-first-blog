from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ("borrador", "Borrador"),
        ("publicado", "Publicado"),
        )
    titulo = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250,
                            unique_for_date = "publicar")
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="blog_posts")
    body = models.TextField()
    publicar = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default ="borrador")

    class Meta:
        ordering = ("-publicar",)

    def __str__(self):
        return self.titulo
