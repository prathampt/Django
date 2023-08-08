from django.shortcuts import render
from markdown2 import Markdown
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util

markdowner = Markdown()

class search(forms.Form):
    q = forms.CharField()

class create(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField(widget=forms.Textarea)

def index(request):
    if request.method == "POST":
        entry = search(request.POST)
        if entry.is_valid():
            q = entry.cleaned_data['q']
            if q in util.list_entries():
                return entryTitle(request, q)
            else:
                return render(request, "encyclopedia/search.html",{
                    "entries": filter(lambda x: q.lower() in x.lower(), util.list_entries()),
                    "q": q
                })
        else:
            return render(request, "encyclopedia/error.html", {
                "key" : 404
            })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryTitle(request, title):
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/error.html", {
                "key" : 404
            })
    return render(request, "encyclopedia/entry.html", {
        "entry": markdowner.convert(entry),
        "title": title
    })

def createNew(request):
    if request.method == "POST":
        add = create(request.POST)
        if add.is_valid():
            title = add.cleaned_data['title']
            content = add.cleaned_data['content']
            if title in list(filter(lambda x: title.lower() in title.lower(), util.list_entries())):
                return render(request, "encyclopedia/error.html")
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("index"),{
                   "entries": util.list_entries() 
                })

    return render(request, "encyclopedia/createpage.html",{
        "form": create()
    })