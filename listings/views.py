from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

def dashboard(request):
    # Fetch all listings, newest first
    listings = Listing.objects.all().order_by('-created_at')
    
    # Handle search/filter by course code if provided
    query = request.GET.get('dept_code')
    if query:
        listings = listings.filter(dept_code__icontains=query.strip())
        
    return render(request, 'dashboard.html', {'listings': listings, 'query': query})

def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ListingForm()
    return render(request, 'create_form.html', {'form': form})