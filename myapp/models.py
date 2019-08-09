from django.db import models
from django.utils import timezone

# Create your models here.
class Youtubejobs(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField(null=False)
    image=models.ImageField(upload_to='images/')
    date=models.DateTimeField('date published', default = timezone.datetime.now())
    writer=models.CharField(max_length=50)
    key=models.CharField(max_length=50)

    def summary(self):
        return self.body[:50]

    # class Meta:
    #     model = Issue        
    #     fields = ['key']
    #     widgets = {
    #         'key' : forms.Select()
    #     }
class Pick(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title