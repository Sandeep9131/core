from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("hey i am django server")
    people = [
       { 'name' : 'abhijeet' , 'age' : 26},
       {'name': 'John', 'age':32},
       {'name':'Jane','age':45},
       {'name':'mhan','age':15},
       {'name':'aohan','age':17},
       {'name':'abhijeet','age':20},
    ]

    vegetables = ['pumpkin' , 'sdbkj' , "dbjq" ,"dhbjq"]
    return render(request , "index.html" , context = { 'people' : people , 'vegetables' : vegetables })

def about(request):
    return render(request , "about.html" )
def contact(request):
    return render(request , "contact.html" )

def success_page(request):
    return HttpResponse("hey this is a sucees page")