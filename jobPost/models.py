from django.db import models


# Create your models here.
class Post(models.Model):
    _id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return str(self.title)
