from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from test_task.api.view import (CreateChannelView, DetailsChannelView,
                                CreateCampaignView, DetailsCampaignView,
                                ListCampaignView, ListChannelView)




urlpatterns = {
    url(r'^channel/$', ListChannelView.as_view(), name="listchannel"),
    url(r'^channel/create/$', CreateChannelView.as_view(), name="createchannel"),
    url(r'^channel/(?P<pk>[0-9]+)/$', DetailsChannelView.as_view(), name="detailschannel"),
    url(r'^campaign/$', ListCampaignView.as_view(), name="listcampaign"),
    url(r'^campaign/create/$', CreateCampaignView.as_view(), name="createcampaign"),
    url(r'^campaign/(?P<pk>[0-9]+)/$', DetailsCampaignView.as_view(), name="detailscampaign"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
