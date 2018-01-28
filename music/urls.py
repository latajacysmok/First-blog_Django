from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<album_id>\d+)/favorite/$', views.favorite, name='favorite'),
    url(r'^new/$', views.album_new, name='album_new'),
    url(r'^edit/(?P<album_id>\d+)/$', views.edit_album, name='edit_album'),
    url(r'^delete/(?P<album_id>\d+)/$', views.delete_album, name='delete_album'),
    url(r'^delete_comment/(?P<comment_id>\d+)/$', views.delete_comment, name='delete_comment'),
    url(r'^edit_comment/(?P<comment_id>\d+)/$', views.edit_comment, name='edit_comment'),
    url(r'^delete_confirmation/(?P<album_id>\d+)/$', views.delete_album_confirmation, name='delete_album_confirmation'),
    url(r'^(?P<album_id>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^profile/(?P<name>\w+)/$', views.user_name, name="user_name"),
    url(r'^songs/$', views.songs, name='songs'),
]
