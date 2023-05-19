from django import forms


class ArtistSearchForm(forms.Form):
    first_name = forms.CharField(
        label="Artist's first name", 
        widget=forms.TextInput(attrs={"type": "text", "autocomplete": "off", "placeholder": " ", "class": "not-required"}),
        required = False,
        max_length=52
        )
    last_name = forms.CharField(
        label="Artist's last name", 
        widget=forms.TextInput(attrs={"type": "text", "autocomplete": "off"}), 
        max_length=52
        )
    

class ArtworkSearchForm(forms.Form):
    artwork_name = forms.CharField(
        label="Artwork name", 
        widget=forms.TextInput(attrs={"type": "text", "autocomplete": "off"}), 
        max_length=100
        )