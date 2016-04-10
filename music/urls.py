from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # Home page /music/
    url(r'^$', views.index, name="index"),

    # Album detail /music/:id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),

    # API for favourite a song /music/:id/favourite/
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name="favourite"),

]
