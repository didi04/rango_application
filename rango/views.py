from django.http import HttpResponse
from django.shortcuts import render

# Construct a dictionary to pass to the template engine as its context
# NB!: boldmessage = {{boldmessage}} from the template
def index(request):
	context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context=context_dict)

# An about view with a link to the index page and a file input
def about(request):
    context_dict = {'authormessage': "This tutorial has been put together by Dilyana Savcheva"}
    return render(request, 'rango/about.html', context=context_dict)