from django.contrib import admin
from django.urls import path
from .views import HomeView
from search_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("search-artist/", views.search_artist, name="search_artist"),
    path("artist/<artist_url>-<artist_id>", views.artist, name="artist"),
    path("search-artwork/", views.search_artwork, name="search_artwork"),
    path("artwork/<artist_name>-<artwork_id>", views.artwork, name="artwork"),
]
