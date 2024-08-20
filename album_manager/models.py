from django.db import models

# Create your models here.
    
class Artist(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    story = models.TextField(default='Historia no disponible')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers')

    def __str__(self):
        return self.title


    
