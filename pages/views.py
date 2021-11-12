from django.shortcuts import render

# Create your views here.
def home_view(request):
	return render(request, "index.html", {})

def products_view(request):
	return render(request, "products.html", {})

def reg_view(request):
	return render(request, "registration.html", {})

def about_view(request):
	return render(request, "about.html", {})

def contacts_view(request):
	return render(request, "contacts.html", {})