from django.test import TestCase, Client
import json
from test_task.api.serializers import ChannelSerializer
from .models import Channel, Campaign
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse

'''ChannelViewTest'''


class ChannelViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.channel_data = {"name": "test", "slug": "test", "bidtypes": ["asflkla", "askflk", "askfl"]}
        self.response = self.client.post(
            reverse('createchannel'),
            self.channel_data,
            format="json")

    def test_api_can_create_a_channel(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_channel(self):
        channel = Channel.objects.get()
        response = self.client.get(
            reverse('detailschannel', kwargs={'pk': channel.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_channel(self):
        change_channel = {"name": "test1", "slug": "test1", "bidtypes": ["askla", "aflk", "askfl"]}
        channel = Channel.objects.get()
        res = self.client.put(
            reverse('detailschannel', kwargs={'pk': channel.pk}),
            change_channel, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_channel(self):
        channel = Channel.objects.get()
        response = self.client.delete(
            reverse('detailschannel', kwargs={'pk': channel.pk}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


'''CampaignViewTest'''


class CampaignViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.channel_data = Channel.objects.create(name="test", slug="test", bidtypes=["asflkla", "askflk", "askfl"])
        self.campaign_data = {"name": "campaign", "channel": self.channel_data.id, "bid": 12.0, "bidType": "askfl"}
        self.response = self.client.post(
            reverse('createcampaign'),
            self.campaign_data,
            format="json")

    def test_api_can_create_a_campaign(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_campaign(self):
        campaign = Campaign.objects.get()
        response = self.client.get(
            reverse('detailschannel', kwargs={'pk': campaign.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_campaign(self):
        change_campaign = {"name": "campaign5", "channel": self.channel_data.id, "bid": 32, "bidType": "asflkla"}
        campaign = Campaign.objects.get()
        res = self.client.put(
            reverse('detailscampaign', kwargs={'pk': campaign.pk}),
            change_campaign, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_campaign(self):
        campaign = Campaign.objects.get()
        response = self.client.delete(
            reverse('detailscampaign', kwargs={'pk': campaign.pk}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
