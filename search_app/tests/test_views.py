from django.test import TestCase, Client
from django.urls import reverse


class SearchArtistTest(TestCase):
    def test_view_by_url_with_parameters(self):
        response = self.client.get("/search-artist/", data={"first_name": "Hieronymus", "last_name": "Bosch"})
        self.assertEqual(response.status_code, 200)

    def test_view_by_name_with_parameters(self):
        response = self.client.get(reverse("search_artist"), data={"first_name": "Hieronymus", "last_name": "Bosch"})
        self.assertEqual(response.status_code, 200)

    def test_view_template_with_parameters(self):
        response = self.client.get(reverse("search_artist"), data={"first_name": "Hieronymus", "last_name": "Bosch"})
        self.assertTemplateUsed(response, "search_app/search.html")
        self.assertContains(response, "Search results for: Hieronymus Bosch", 1, 200)

    def test_view_by_url_no_parameters(self):
        response = self.client.get("/search-artist/")
        self.assertEqual(response.status_code, 200)

    def test_view_by_name_no_parameters(self):
        response = self.client.get(reverse("search_artist"))
        self.assertEqual(response.status_code, 200)

    def test_view_template_no_parameters(self):
        response = self.client.get(reverse("search_artist"))
        self.assertTemplateUsed(response, "search_app/search.html")
        self.assertContains(response, "No search results for:", 1, 200)

    
class ArtistTest(TestCase):
    def setUp(self):
        self.client = Client(raise_request_exception=False)

    def test_view_by_url_with_parameters(self):
        response = self.client.get("/artist/hieronymus-bosch-57726d7fedc2cb3880b481c6")
        self.assertEqual(response.status_code, 200)

    def test_view_by_name_with_parameters(self):
        response = self.client.get(reverse("artist", kwargs={"artist_url": "hieronymus-bosch", "artist_id": "57726d7fedc2cb3880b481c6"}))
        self.assertEqual(response.status_code, 200)

    def test_view_template_with_parameters(self):
        response = self.client.get(reverse("artist", kwargs={"artist_url": "hieronymus-bosch", "artist_id": "57726d7fedc2cb3880b481c6"}))
        self.assertTemplateUsed(response, "search_app/artist.html")
        self.assertContains(response, "Hieronymus Bosch", 2, 200)

    def test_view_by_url_no_parameters(self):
        response = self.client.get("/artist/")
        self.assertEqual(response.status_code, 404)

    def test_view_by_name_invalid_artist_url_parameter(self):
        response = self.client.get(reverse("artist", kwargs={"artist_url": "x-y", "artist_id": "57726d7fedc2cb3880b481c6"}))
        self.assertEqual(response.status_code, 500)

    def test_view_by_name_invalid_artist_id_parameter(self):
        response = self.client.get(reverse("artist", kwargs={"artist_url": "hieronymus-bosch", "artist_id": "123"}))
        self.assertEqual(response.status_code, 500)


class SearchArtworkTest(TestCase):
    def test_view_by_url_with_parameter(self):
        response = self.client.get("/search-artwork/", data={"artwork_name": "Mona Lisa"})
        self.assertEqual(response.status_code, 200)

    def test_view_by_name_with_parameter(self):
        response = self.client.get(reverse("search_artwork"), data={"artwork_name": "Mona Lisa"})
        self.assertEqual(response.status_code, 200)

    def test_view_template_with_parameter(self):
        response = self.client.get(reverse("search_artwork"), data={"artwork_name": "Mona Lisa"})
        self.assertTemplateUsed(response, "search_app/search.html")
        self.assertContains(response, "Search results for: Mona Lisa", 1, 200)

    def test_view_by_url_no_parameter(self):
        response = self.client.get("/search-artwork/")
        self.assertEqual(response.status_code, 200)

    def test_view_by_name_no_parameter(self):
        response = self.client.get(reverse("search_artwork"))
        self.assertEqual(response.status_code, 200)

    def test_view_template_no_parameter(self):
        response = self.client.get(reverse("search_artwork"))
        self.assertTemplateUsed(response, "search_app/search.html")
        self.assertContains(response, "No search results for:", 1, 200)


class ArtworkTest(TestCase):
    def setUp(self):
        self.client = Client(raise_request_exception=False)

    def test_view_by_url_with_parameters(self):
        response = self.client.get("/artwork/Leonardo%20da%20Vinci-57727444edc2cb3880cb7bf6")
        self.assertEqual(response.status_code, 200)

    def test_view_by_name_with_parameters(self):
        response = self.client.get(reverse("artwork", kwargs={"artwork_id": "57727444edc2cb3880cb7bf6", "artist_name": "Leonardo da Vinci"}))
        self.assertEqual(response.status_code, 200)

    def test_view_template_with_parameters(self):
        response = self.client.get(reverse("artwork", kwargs={"artwork_id": "57727444edc2cb3880cb7bf6", "artist_name": "Leonardo da Vinci"}))
        self.assertTemplateUsed(response, "search_app/artwork.html")
        self.assertContains(response, "Mona Lisa", 7, 200)

    def test_view_by_url_no_parameters(self):
        response = self.client.get("/artwork/")
        self.assertEqual(response.status_code, 404)

    def test_view_by_name_invalid_artwork_id_parameter(self):
        response = self.client.get(reverse("artwork", kwargs={"artwork_id": "123", "artist_name": "Leonardo da Vinci"}))
        self.assertEqual(response.status_code, 500)
