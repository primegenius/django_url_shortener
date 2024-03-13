from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Links
from django.urls import reverse
from .forms import LinkForm

# Create your views here.
def index(request):
    links = Links.objects.all()
    context = {
        "links": links,
    }

    return render(request, 'index.html', context)

def root_link(request, link_slug):
    link = get_object_or_404(Links, slug=link_slug)

    return redirect(link.url)

def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = LinkForm()
        context = {
            "form": form
        }
    return render(request, 'create.html', context)