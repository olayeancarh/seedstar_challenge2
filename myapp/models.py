from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class seedStars(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    email = models.EmailField(verbose_name=_('Email address'), unique=True, max_length=255,)

    def __str__(self):
        return self.name