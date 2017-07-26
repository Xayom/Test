from rest_framework import serializers
from test_task.models import Channel, Campaign


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'slug', 'bidtypes')


class CampaignListSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only=True)

    class Meta:
        model = Campaign
        fields = ('name', 'channel', 'bid', 'bidType')


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('name', 'channel', 'bid', 'bidType')
