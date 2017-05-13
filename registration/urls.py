from django.conf.urls import url

from .views import sign_in, sign_up, sign_out, edit_profile

urlpatterns = [
    url(r'^sign-in/$', sign_in, name='sign_in'),
    url(r'^sign-up/$', sign_up, name='sign_up'),
    url(r'^sign-out/$', sign_out, name='sign_out'),
    url(r'^edit-profile/$', edit_profile, name='edit_profile')
]
