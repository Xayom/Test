from django.test import TestCase
from .models import Channel, Campaign
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

'''ChannelViewTest'''


class ChannelViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.channel_data = {'name': 'Go Go'}
        self.response = self.client.post(
            reverse('create'),
            self.channel_data,
            format="json")

    def test_api_can_create_a_channel(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_channel(self):
        channel = Channel.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': channel.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, channel)

    def test_api_can_update_channel(self):
        change_channel = {'name': 'Something new'}
        channel = Channel.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': channel.id}),
            change_channel, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_channel(self):
        channel = Channel.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': channel.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


'''CampaignViewTest'''


class CampaignViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.campaign_data = {'name': 'Go Go'}
        self.response = self.client.post(
            reverse('create'),
            self.campaign_data,
            format="json")

    def test_api_can_create_a_campaign(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_campaign(self):
        campaign = Campaign.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': campaign.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, campaign)

    def test_api_can_update_campaign(self):
        change_campaign = {'name': 'Something new'}
        campaign = Campaign.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': campaign.id}),
            change_campaign, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_campaign(self):
        campaign = Campaign.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': campaign.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
