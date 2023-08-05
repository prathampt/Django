from django.shortcuts import render
from markdown2 import Markdown
from django import forms
from . import util

markdowner = Markdown()

class search(forms.Form):
    q = forms.CharField()

def index(request):
    if request.method == "POST":
        entry = search(request.POST)
        if entry.is_valid():
            q = entry.cleaned_data['q']
            try:
                return entryTitle(request, q)
            except Exception as e:
                return render(request, "encyclopedia/error.html")
        else:
            return render(request, "encyclopedia/error.html")

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryTitle(request, title):
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/entry.html", {
        "entry": markdowner.convert(entry),
        "title": title
    })

