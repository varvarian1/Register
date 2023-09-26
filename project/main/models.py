from django.db import models

# Create your models here.

class Reger(models.Model):
    email = models.EmailField('Почта', max_length=50, default='')
    password = models.CharField('Пороль', max_length=100, default='')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Register'
        verbose_name_plural = 'Registration'