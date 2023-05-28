import requests
    

def get_paginated_data(url):
    """Function checks if response data has pagination and if so ads data from all pages. Returns data in JSON format"""
    response = requests.get(url=url).json()
    data = response["data"]
    while response["hasMore"]:
        pagination_token = response["paginationToken"]
        response = requests.get(url=url + f"&paginationToken={pagination_token}").json()
        data += response["data"]
    return data
