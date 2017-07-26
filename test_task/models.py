from django.db import models

bid_choices = (
    ('cpc', 'cost per click'),
    ('cpm', 'cost per mile'),
    ('cpa', 'cost per action'),
    ('cpv', 'cost per view'),
    ('cpi', 'cost per install'),
)


class Channel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=15)
    bidtypes = models.CharField(max_length=50, choices=bid_choices)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=50)
    channel = models.ForeignKey(Channel)
    bid = models.FloatField()
    bidType = models.CharField(max_length=15)
