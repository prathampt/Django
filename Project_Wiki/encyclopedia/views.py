from django.shortcuts import render
from markdown2 import Markdown
from . import util

markdowner = Markdown()

def index(request):
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

