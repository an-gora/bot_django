from django.db import models

class Ad(models.Model):
    title = models.TextField(verbose_name='Ads title', max_length=500)
    # city = models.ForeignKey(City, on_delete=models.PROTECT, default=None)
    city = models.CharField(verbose_name='City', max_length=150, blank=True)
    price = models.CharField(verbose_name='Price for rent', max_length=150, blank=True)
    # price = models.PositiveIntegerField(verbose_name='Price for appartment', default=None)
    metrs = models.CharField(verbose_name='City', max_length=150, blank=True)
    # url = models.URLField(verbose_name='Url to ad')
    url = models.URLField(verbose_name='Url to ad', unique=True)

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = "Ads"

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Subscriber(models.Model):
    chat_id = models.CharField(unique=True, max_length=150)
    
    def __str__(self):
        return f'{self.title}'
