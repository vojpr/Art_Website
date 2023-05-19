from django.test import TestCase
from homepage.forms import ArtistSearchForm, ArtworkSearchForm


class ArtistSearchFormTest(TestCase):
    def test_labels(self):
        form = ArtistSearchForm()
        self.assertAlmostEqual(form.fields["first_name"].label, "Artist's first name")
        self.assertAlmostEqual(form.fields["last_name"].label, "Artist's last name")

    def test_valid(self):
        form = ArtistSearchForm(data={"first_name": "", "last_name": "Last Name"})
        self.assertTrue(form.is_valid())

    def test_invalid_missing_last_name(self):
        form = ArtistSearchForm(data={"first_name": "First Name", "last_name": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["last_name"], ["This field is required."])


class ArtworkSearchFormTest(TestCase):
    def test_label(self):
        form = ArtworkSearchForm()
        self.assertAlmostEqual(form.fields["artwork_name"].label, "Artwork name")

    def test_valid(self):
        form = ArtworkSearchForm(data={"artwork_name": "Artwork name"})
        self.assertTrue(form.is_valid())

    def test_invalid_missing_artwork_name(self):
        form = ArtworkSearchForm(data={"artwork_name": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["artwork_name"], ["This field is required."])
