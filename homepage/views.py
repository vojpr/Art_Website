from django.views.generic import TemplateView
import requests
import random
from utils.constants import REQUEST_MOST_VIEWED_PAINTINGS
from .forms import ArtistSearchForm, ArtworkSearchForm


class HomeView(TemplateView):
    template_name = "homepage/index.html"

    def get_context_data(self,*args, **kwargs):
        # Use API for most viewed paintings to show in the inspiration section
        response = requests.get(url=REQUEST_MOST_VIEWED_PAINTINGS)
        inspiration_data = response.json()["data"]
        pagination_token = response.json()['paginationToken']
        for each in range(2):
            response = requests.get(url=REQUEST_MOST_VIEWED_PAINTINGS + f"?paginationToken={pagination_token}")
            inspiration_data += response.json()["data"]
            pagination_token = response.json()['paginationToken']
        random.shuffle(inspiration_data)
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context["inspiration_data"] = inspiration_data
        context["artist_search_form"] = ArtistSearchForm()
        context["artwork_search_form"] = ArtworkSearchForm()
        return context
