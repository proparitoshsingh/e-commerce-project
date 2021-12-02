from django.shortcuts import render

navbar_context = {"uname":"Login/Sign Up"}

# Create your views here.
def home_view(request):
	return render(request, "index.html", navbar_context)

def about_view(request):
	return render(request, "about.html", navbar_context)

def contacts_view(request):
	return render(request, "contacts.html", navbar_context)