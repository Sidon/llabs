from django.db import models


class Person(models.Model):
    facebookId = models.IntegerField(verbose_name='Id', primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Name', blank=True)
    gender = models.CharField(max_length=1, verbose_name='Gender', blank=True)
    email = models.CharField(max_length=255, verbose_name='email', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Facebook Users'


