from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)
    format = models.CharField(max_length=50, blank=True, null=None)
    photo = models.ImageField(upload_to='photos')
    photo_mod = models.ImageField(upload_to='photos_mod',
                                  blank=True,
                                  null=None
                                  )
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.title