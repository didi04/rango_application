from django.http import HttpResponse 

# An inital view (index view) with a link to the about page
def index(request):
	return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

# An about view with a link to the index page
def about(request):
	return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>Index</a>")
