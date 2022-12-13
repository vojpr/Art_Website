import requests


def add_all_pages(response, data, url):
    """Function checks if response data has pagination and if so ads data from all pages. Returns data in JSON format"""
    if response.json()["hasMore"]:
        pagination_token = response.json()['paginationToken']
        response = requests.get(url=url + f"&paginationToken={pagination_token}")
        data += response.json()["data"]
        return add_all_pages(response, data, url)
    else:
        return data