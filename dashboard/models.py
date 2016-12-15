from django.db import models
from django.core.urlresolvers import reverse

class Dictionary(models.Model):
    title = models.CharField(max_length=100)
    logo = models.FileField(null=True)

    def get_absolute_url(self):
        return reverse('dashboard:dict', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Word(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, null=True)
    english = models.CharField(max_length=50)
    polish = models.CharField(max_length=100)


    def __str__(self):
        return self.english + " - " + self.polish