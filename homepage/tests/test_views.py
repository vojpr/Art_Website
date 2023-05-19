from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_view_by_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "homepage/index.html")
        self.assertContains(response, "Your online art gallery", 1, 200)
