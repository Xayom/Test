from django.contrib import admin
from .models import Channel, Campaign


class CampaignInline(admin.StackedInline):
    model = Campaign


class ChannelInline(admin.StackedInline):
    model = Channel
    inlines = [CampaignInline]


admin.site.register(Channel, ChannelInline)
admin.site.register(Campaign)
