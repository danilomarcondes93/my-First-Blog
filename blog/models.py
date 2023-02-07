from django.conf import settings
from django.db import models
from django.utils import timezone


# models.Model significa que o Post é um modelo de Django, então o Django sabe que ele deve ser salvo no banco de dados.
class Post(models.Model):
    # este é um link para outro modelo
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # é assim que definimos um texto com um número limitado de caracteres.
    title = models.CharField(max_length=200)
    text = models.TextField()  # Texto sem limite de caracteres
    # este é uma data e hora.
    created_date = models.DateTimeField(default=timezone.now)
    # este é uma data e hora.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
