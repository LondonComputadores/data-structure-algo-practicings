from django.shortcuts import render
from django.http import HttpResponse


# CLASS BASED VIEWS

# V1

from .models import Book
from django.views.generic import ListView
from .decorators import login_required


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book
    context_object_name = 'books'

# @login_required
def book_detail(request, slug):

    if request.method == 'GET':
        return HttpResponse("detail view")

    elif request.method == 'POST':
        return HttpResponse("add view")

    elif request.method == 'PUT':
        return HttpResponse("edit view")    

    elif request.method == 'DELETE':
        return HttpResponse("delete view")

###############################################################################

# FUNCTIONS BASED VIEWS

# V3 Code

def index(request):
    return render(request, 'index.html')

# def book_detail(request, slug):

#     if request.method == 'GET':
#         return HttpResponse("detail view")

#     elif request.method == 'POST':
#         return HttpResponse("add view")

#     elif request.method == 'PUT':
#         return HttpResponse("edit view")    

#     elif request.method == 'DELETE':
#         return HttpResponse("delete view")


# V2 Code

# def book_list(request):
#     return HttpResponse("list view")

# def book_detail(request, slug):

#     if request.method == 'GET':
#         return HttpResponse("detail view")

#     elif request.method == 'POST':
#         return HttpResponse("add view")

#     elif request.method == 'PUT':
#         return HttpResponse("edit view")    

#     elif request.method == 'DELETE':
#         return HttpResponse("delete view")
    


# V1 Code

# def book_list(request):
#     return HttpResponse("list view")

# def book_detail(request, slug):
#     return HttpResponse("detail view")

# def book_add(request):
#     return HttpResponse("add view")

# def book_delete(request, slug):
#     return HttpResponse("delete view")

# def book_edit(request, slug):
#     return HttpResponse("edit view")