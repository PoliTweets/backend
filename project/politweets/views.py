from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(request):
    context = RequestContext(request)
    context_dict = {"title": ("Politweets")}
    return render_to_response('polytweets/index.html', context_dict, context)
