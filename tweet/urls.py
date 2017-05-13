from django.conf.urls import url

from .views import add_tweet

urlpatterns = [
    url(r'^add/$', add_tweet, name='add_tweet')
]
