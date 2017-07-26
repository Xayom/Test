from django.test import TestCase
from .models import Channel, Campaign
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ViewTestCase(TestCase):
    def setUp(self):
        pass

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
            reverse('details', kwargs={'pk': Channel.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
