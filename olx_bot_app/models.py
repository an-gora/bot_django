from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=500)
    city = models.ForeignKey(City, on_delete=models.PROTECT, default=None)
    price = models.PositiveIntegerField(default=None)
    address = models.CharField(max_length=150, blank=True)
    metrs = models.FloatField(default=None)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Subscriber(models.Model):
    chat_id = models.CharField(unique=True, max_length=150)
    
    def __str__(self):
        return f'{self.title}'
