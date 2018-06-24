from django.urls import path

from dialogbot.views import (
    IndexView, OauthCallbackView, CommandView, InteractionView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('oauth-callback/', OauthCallbackView.as_view(), name='oauth_callback'),
    path('command/', CommandView.as_view(), name='command'),
    path('interaction/', InteractionView.as_view(), name='command'),
]
