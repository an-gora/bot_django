from django.db import models


# class City(models.Model):
#     name = models.CharField(max_length=200, unique=False)
#
#     def __str__(self):
#         return self.name


class Ad(models.Model):
    title = models.TextField(verbose_name='Ads title', max_length=500)
    # city = models.ForeignKey(City, on_delete=models.PROTECT, default=None)
    city = models.CharField(verbose_name='City', max_length=150, blank=True)
    price = models.PositiveIntegerField(verbose_name='Price for appartment', default=None)
    metrs = models.FloatField(verbose_name='Square of appartment',default=None)
    url = models.URLField(verbose_name='Url to ad', null=True, blank=True)

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
