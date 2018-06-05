from django.db import models

# Create your models here.


class music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'music'


class travel(models.Model):
    location = models.TextField()
    time = models.DateTimeField()

    class Meta:
        db_table = 'travel'