from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import ChannelSerializer, CampaignSerializer, CampaignListSerializer
from test_task.models import Channel, Campaign

'''Channel API views'''


class CreateChannelView(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsChannelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ListChannelView(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


'''Campaign API views'''


class CreateCampaignView(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsCampaignView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class ListCampaignView(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignListSerializer
