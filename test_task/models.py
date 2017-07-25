from django.db import models

bid_choices = (
    ('cpc', 'cpc')
    ('cpm', 'cpm')
    ('cpa', 'cpa')
    ('cpv', 'cpv')
    ('cpi', 'cpi')
)


class Channel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    bidtypes = models.CharField(choices=bid_choices)


class Campaign(models.Model):
    name = models.CharField(max_length=50)
    channel = models.ForeignKey(Channel)
    bid = models.FloatField()
    bidType = models.CharField()
