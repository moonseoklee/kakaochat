from django.conf.urls import url

urlpatterns = [
    url(r'^keyboard/',inform.views.keyboard),
    url(r'^message',inform.views.message),
]