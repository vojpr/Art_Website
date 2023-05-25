from django.test import TestCase
from django.urls import reverse


class SearchArtistTest(TestCase):
    def test_view_by_url_with_query_string(self):
        response = self.client.get("/search-artist/", data={"first_name": "pablo", "last_name": "picasso"})
        self.assertEqual(response.status_code, 200)

    def test_view_by_name_with_query_string(self):
        response = self.client.get(reverse("search_artist"), data={"first_name": "pablo", "last_name": "picasso"})
        self.assertEqual(response.status_code, 200)

    def test_view_template_with_query_string(self):
        response = self.client.get(reverse("search_artist"), data={"first_name": "pablo", "last_name": "picasso"})
        self.assertTemplateUsed(response, "search_app/search.html")
        self.assertContains(response, "Search results for: pablo picasso", 1, 200)

    def test_view_by_url_no_query_string(self):
        response = self.client.get("/search-artist/")
        self.assertEqual(response.status_code, 200)

    def test_view_by_name_no_query_string(self):
        response = self.client.get(reverse("search_artist"))
        self.assertEqual(response.status_code, 200)

    def test_view_template_no_query_string(self):
        response = self.client.get(reverse("search_artist"))
        self.assertTemplateUsed(response, "search_app/search.html")
        self.assertContains(response, "No search results for:", 1, 200)



