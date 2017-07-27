from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=15)
    slug = models.CharField(max_length=15)
    bidtypes = ArrayField(models.CharField(max_length=50))

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=15)
    channel = models.ForeignKey(Channel)
    bid = models.FloatField()
    bidType = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.bidType not in self.channel.bidtypes:
            raise ValidationError("Bidtype should be in bidtypes channel")
        super(Campaign, self).save(*args, **kwargs)
