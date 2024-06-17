from django.conf import settings
from django.db import models
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #C'est un lien vers un autre modèle.
    title = models.CharField(max_length=200) #  définir un champ texte avec un nombre limité de caractères.
    text = models.TextField() #définir un champ text sans limite de caractères.
    created_date = models.DateTimeField(default=timezone.now) #Définit que le champ en question est un horodatage (date et heure).
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title