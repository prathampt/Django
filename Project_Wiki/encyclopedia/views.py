from django.shortcuts import render
from markdown2 import Markdown
from django import forms
from . import util

markdowner = Markdown()

class search(forms.Form):
    q = forms.CharField()

class new():
    pass

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
        title = new(request.POST)
        if title.is_valid():
            q = entry.cleaned_data['q']
            if q in list(filter(lambda x: q.lower() in x.lower(), util.list_entries())):
                return render(request, "encyclopedia/error.html")
            else:
                pass

    return render(request, "encyclopedia/createpage.html")