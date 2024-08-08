# Ingresar tus URLs de la app aquí
from django.urls import path

from . import views

app_name = "album_manager"

urlpatterns = [
    path("", views.index, name="index"),
    
    path("artist/", views.artist, name="artist"),
    path("artist/add_artist/", views.add_artist, name="add_artist"),
    path("artist/<str:artist_name>/", views.display_artist, name="display_artist"),
    path("artist/edit_artist/<str:artist_name>/", views.edit_artist, name="edit_artist"),
    path("artist/delete_artist/<str:artist_name>/", views.delete_artist, name="delete_artist"),
    
    path("album/", views.album, name="album"),
    path("album/add_album/", views.add_album, name="add_album"),
    path("album/<str:album_title>/", views.display_album, name="display_album"),
    path("album/edit_album/<str:album_title>/", views.edit_album, name="edit_album"),
    path("album/delete_album/<str:album_title>/", views.delete_album, name="delete_album"),
]