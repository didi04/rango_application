from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

# Construct a dictionary to pass to the template engine as its context
# NB!: boldmessage = {{boldmessage}} from the template
def index(request):
	#context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}
	#return render(request, 'rango/index.html', context=context_dict)

# Query the database for a list of ALL categories currently stored.
# Order the categories by no. likes in descending order.
# Retrieve the top 5 only - or all if less than 5.
# Place the list in our context_dict dictionary
# that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

# Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)

# An about view with a link to the index page and a file input
def about(request):
    context_dict = {'authormessage': "This tutorial has been put together by Dilyana Savcheva"}
    return render(request, 'rango/about.html', context=context_dict)