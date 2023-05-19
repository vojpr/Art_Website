from django.shortcuts import render
import unidecode
import re
import random
import requests
import random
from utils.constants import REQUEST_PAINTING_BY_NAME_URL, REQUEST_ARTIST_URL, REQUEST_PAINTING_BY_ARTIST_ID_URL, \
    REQUEST_PAINTING_BY_ID_URL, REQUEST_ARTIST_PARAMS
from utils.functions import add_all_pages


def search_artist(request):
    first_name = request.GET['first_name']
    if first_name != "":
        first_name = first_name + " "
    last_name = request.GET['last_name']
    searched_name = first_name + last_name
    # Replace any spaces with dashes and convert unicode to ascii
    name_url = unidecode.unidecode(searched_name.replace(' ', '-').lower())
    # API for artist search by name not created by Wikiart yet
    # Use API for painting search by name instead and extract relevant data (artist name and ID)
    url = REQUEST_PAINTING_BY_NAME_URL + name_url
    response = requests.get(url=url)
    paintings_data = response.json()["data"]
    artists_found = []
    for painting in paintings_data:
        if name_url in painting["artistUrl"] and {"artistUrl": painting["artistUrl"], "artistId": painting["artistId"]} not in artists_found:
            artists_found.append({"artistUrl": painting["artistUrl"], "artistId": painting["artistId"]})
    # Use API to search for artists details using each "artistURL"
    artists_details = []
    for artist in artists_found:
        count = 0
        url = REQUEST_ARTIST_URL + artist["artistUrl"]
        response = requests.get(url=url, params=REQUEST_ARTIST_PARAMS)
        artist_data = response.json()
        # Merge all data about an artist into one dictionary
        artist_data["artistUrl"] = artists_found[count]["artistUrl"]
        artist_data["artistId"] = artists_found[count]["artistId"]
        artists_details.append(artist_data)
        count += 1
    context = {
        "search": "artist",
        "searched_name": searched_name,
        "artists_details": artists_details,
    }
    return render(request, "search_app/search.html", context=context)


def artist(request, artist_url, artist_id):
    # Use API to search for artist details using "artistURL"
    url = REQUEST_ARTIST_URL + artist_url
    response = requests.get(url=url, params=REQUEST_ARTIST_PARAMS)
    data = response.json()
    if data["biography"]:
        # Convert biography to plain text
        biography = re.sub("[\(\[].*?[\)\]]", "", data["biography"])
    else:
        biography = ""
    # Use API to search for paintings using "artistID"
    paintings_url = REQUEST_PAINTING_BY_ARTIST_ID_URL + artist_id
    paintings_response = requests.get(url=paintings_url)
    paintings_data = paintings_response.json()["data"]
    # Get paintings from all pages in case of pagination
    paintings_data = add_all_pages(paintings_response, paintings_data, paintings_url)
    random.shuffle(paintings_data)
    context = {
        "data": data,
        "biography": biography,
        "paintings_data": paintings_data,
    }
    return render(request, "search_app/artist.html", context=context)


def search_artwork(request):
    searched_artwork = request.GET['artwork_name']
    # Replace any spaces with dashes and convert unicode to ascii
    searched_artwork_url = unidecode.unidecode(searched_artwork.replace(' ', '-').lower())
    # Use API to search paintings by name
    url = REQUEST_PAINTING_BY_NAME_URL + searched_artwork_url
    response = requests.get(url=url)
    artworks_data = response.json()["data"]
    # Sort by completion year
    artworks_data = sorted(artworks_data, key=lambda each: str(each['completitionYear']))
    context = {
        "search": "artwork",
        "searched_artwork": searched_artwork,
        "artworks_data": artworks_data,
    }
    return render(request, "search_app/search.html", context=context)


def artwork(request, artwork_id, artist_name):
    # Use API to search for painting details using artwork id
    url = REQUEST_PAINTING_BY_ID_URL + artwork_id
    response = requests.get(url=url)
    data = response.json()
    if data["description"]:
        # Convert description to plain text
        description = re.sub("[\(\[].*?[\)\]]", "", data["description"])
    else:
        description = ""
    context = {
        "data": data,
        "description": description,
        "artist_name": artist_name,
    }
    return render(request, "search_app/artwork.html", context=context)
