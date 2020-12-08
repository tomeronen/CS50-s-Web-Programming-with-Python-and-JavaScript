from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def show_wiki(request, wiki_title):
    wiki_markdown = util.get_entry(wiki_title)
    wiki_exists = wiki_markdown is not None
    if wiki_exists:
        wiki_content = markdown2.markdown(util.get_entry(wiki_title))
    else:
        wiki_content = ""

    return render(request, "encyclopedia/wiki.html", {
        "wiki_content": wiki_content,
        "wiki_title": wiki_title,
        "wiki_exists": wiki_exists
    })


def search_wiki(request):
    query = request.GET.get('q', '')
    wiki_names = util.list_entries()
    res = [i for i in wiki_names if query in i]
    return render(request, "encyclopedia/search.html", {
        "wiki_names": res
    })
