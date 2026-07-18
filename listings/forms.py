from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'dept_code', 'listing_type', 'condition', 'contact_email']