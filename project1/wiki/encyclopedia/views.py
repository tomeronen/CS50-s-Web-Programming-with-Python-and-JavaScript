from django.shortcuts import render
import markdown2
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def show_wiki(request, wiki_title):
    wiki_content = markdown2.markdown(util.get_entry(wiki_title))
    return render(request, "encyclopedia/wiki.html", {
        "wiki_content": wiki_content,
        "wiki_title": wiki_title
    })
