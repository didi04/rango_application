from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

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
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': pages_list}

# Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)

# An about view with a link to the index page and a file input
def about(request):
    context_dict = {'authormessage': "This tutorial has been put together by Dilyana Savcheva"}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict ={}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)
