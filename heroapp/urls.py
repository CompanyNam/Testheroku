from django.conf.urls import url
from .views import index_view

app_name = "heroapp"

urlpatterns = [
    url(r'^index/$', index_view, name="index"),
]
