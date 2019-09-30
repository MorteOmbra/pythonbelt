from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.contrib import messages
from .models import User, Quote
import bcrypt

def main_page(request):
    return render(request,"main.html")
    
def register(request):
    errors = User.objects.registration_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/")
    password = request.POST['password']
    hashword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    decode = hashword.decode()
    new_user = User.objects.create(name = request.POST['name'], email = request.POST['email'], password = decode)
    request.session['id'] = new_user.id
    return redirect("/quotes")

def login(request):
    errors = User.objects.login_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    request.session['id'] = User.objects.filter(email = request.POST['email'])[0].id
    return redirect("/quotes")

def quotes(request):
    user = User.objects.get(id = request.session['id'])
    quote = Quote.objects.exclude(favorited = user).all
    favorite = Quote.objects.filter(favorited = user) #I only want quotes favorited by this user
    context = {
        "user": user,
        "quote": quote,
        "favorite": favorite
    }
    
    return render(request, "quotes.html", context)

def add_quote(request):
    errors = Quote.objects.quote_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/quotes")
    user = User.objects.get(id = request.session['id'])
    new_quote = Quote.objects.create(source = request.POST['source'], content = request.POST['content'], poster = user)
    return redirect("/quotes")

def logout(request):
    request.session.clear()
    return redirect("/")

def show_user(request,x):
    user = User.objects.get(id = x)

    def first_name(user):
        name = user.name
        name_string = ""
    
        for x in range(len(name)):
            if name[x] != " ":
                name_string += name[x]
            elif name[x] == " ":
                break
        return name_string

    name = first_name(user)
    end = user.name[0]
    all_quotes = user.quotes.all()
    
    length = len(all_quotes)
    context = {
        "user": user,
        "end": end,
        "length": length,
        "name": name,
        "all_quotes": all_quotes
    }
    return render(request, "show_user.html", context)

def delete_this(request, x):
    quote = Quote.objects.get(id = x)
    quote.delete()
    return redirect("/quotes")

def edit_quote(request,x):
    quote = Quote.objects.get(id = x)
    print(type(quote))
    context = {
        "quote": quote
    }
    return render(request, "edit_quote.html", context)

def update(request, x):
    quote = Quote.objects.get(id = x)
    quote.source = request.POST['source']
    quote.content = request.POST['content']
    quote.save()
    return redirect("/quotes")

def add_favorite(request, x):
    user = User.objects.get(id = request.session['id'])
    quote = Quote.objects.get(id = x)
    user.favorite_quotes.add(quote)
    return redirect("/quotes") 

def remove_favorite(request, x):
    user = User.objects.get(id = request.session['id'])
    quote = Quote.objects.get(id = x)
    user.favorite_quotes.remove(quote)
    return redirect("/quotes") 