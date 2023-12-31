from django.shortcuts import render
from markdown2 import Markdown
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
import random

markdowner = Markdown()

class search(forms.Form):
    q = forms.CharField()

class create(forms.Form):
    title = forms.CharField(max_length=20, label="Title",widget=forms.TextInput(attrs={'class':"form-control", 'id':"exampleFormControlInput1"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'id':"exampleFormControlTextarea1", 'rows':"10",'cols':'20','placeholder':"Write the **markdown** text like #this here."}), label="Content")

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
    entry = str(util.get_entry(title)).strip()
    if not entry:
        return render(request, "encyclopedia/error.html", {
                "key" : 404
            })
    return render(request, "encyclopedia/entry.html", {
        "entry": str(markdowner.convert(entry)).strip(),
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
                util.save_entry(title, f"# {title}\n\n" + content)
                return entryTitle(request, title)

    return render(request, "encyclopedia/createpage.html",{
        "form": create(),
        "action": "Submit"
    })

def edit(request, title):
    if request.method == "POST":
        add = create(request.POST)
        if add.is_valid():
            title = add.cleaned_data['title']
            content = str(add.cleaned_data['content']).strip()
            util.save_entry(title, content)
            return entryTitle(request, title)

    entry = str(util.get_entry(title))
    return render(request, "encyclopedia/createpage.html",{
    "form": create({'title':f"{title}", 'content':f"{entry.strip()}"}),
    "title": title
})


def Random(request):
    title = random.choice(util.list_entries())
    entry = util.get_entry(title)
    
    return render(request, "encyclopedia/entry.html", {
        "entry": markdowner.convert(entry),
        "title": title
    })