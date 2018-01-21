from django.http import HttpResponse
from django.shortcuts import render

# Construct a dictionary to pass to the template engine as its context
# NB!: boldmessage = {{boldmessage}} from the template
def index(request):
	context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context=context_dict)

# An about view with a link to the index page
def about(request):
	return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>Index</a>")
