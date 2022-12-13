from django.views.generic import TemplateView
import requests
import random
from utils.constants import REQUEST_MOST_VIEWED_PAINTINGS


class HomeView(TemplateView):
    template_name = "index.html"
    # Use API for most viewed paintings to show in the inspiration section
    response = requests.get(url=REQUEST_MOST_VIEWED_PAINTINGS)
    inspiration_data = response.json()["data"]
    pagination_token = response.json()['paginationToken']
    for each in range(2):
        response = requests.get(url=REQUEST_MOST_VIEWED_PAINTINGS + f"?paginationToken={pagination_token}")
        inspiration_data += response.json()["data"]
        pagination_token = response.json()['paginationToken']
    random.shuffle(inspiration_data)

    extra_context = {
        "inspiration_data": inspiration_data,
    }
