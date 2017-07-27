from django.contrib import admin
from .models import Channel, Campaign


class CampaignInline(admin.StackedInline):
    model = Campaign


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        CampaignInline,
    ]


admin.site.register(Channel, AuthorAdmin)
admin.site.register(Campaign)
