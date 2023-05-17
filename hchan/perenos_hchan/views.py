from django.shortcuts import render
from .models import * 
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.

def index (req):
    cards = Card.objects.order_by('id')
    context = {'cards': cards}
    return render(req, "perenos_hchan/main_page.html", context)

def profile(req):
    user = Person.objects.get(id=1)
    context = {'user': user}
    return render(req, "perenos_hchan/profile.html", context)

def collection(req):
    cards = Collection.objects.all()
    coll = []

    for i in cards:
        if i.person_id.id == 1:
            coll.append(i)
        
    context = {'cards': tuple(coll)}
    return render(req, "perenos_hchan/collectin.html", context)

def brother(req):
    manga = Collection.objects.all()

    mangas = ''
    for i in manga:
        if i.card_id.id == 1:
            mangas = i
            break

    context = {'manga': mangas}
    return render(req, "perenos_hchan/brother_no_brother.html", context)

def manga(req):
    page = Manga.objects.all()

    pages = []
    first = ''

    for i in page:
        if i.manga_id.id == 1:
            pages.append(i)

    first = pages[0]

    context = {'pages': tuple(pages[1:]), 'first': first}
    return render(req, "perenos_hchan/manga.html", context)

def home(req):
    return render(req, 'user/home.html')


class SignUp(CreateView):
    form_class = UserCreationForm
    seccess_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



