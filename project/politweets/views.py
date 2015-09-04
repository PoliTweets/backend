from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import models
import forms

def index(request):
    context = RequestContext(request)

    if request.method == 'GET':
        CHOICES = (
            ("pdc", "PDC"),
            ("plr", "PDC"),
            ("gre", "Les Verts"),
            ("udc", "UDC"),
        )

        form = forms.ResultCreateForm(choices=CHOICES, initial=[gender[0] for gender in CHOICES])
        context_dict = {"title": "Politweets", "form": form}
        return render_to_response('polytweets/index.html', context_dict, context)
    else:
        form = forms.ResultCreateForm(request.POST) # Bind data from request.POST into a PostForm

        if form.is_valid():
            answer = form.cleaned_data['answer']
            # return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))

        context_dict = {"title": "Politweets", "form": form}
        return render_to_response(request, 'polytweets/index.html', context_dict, context)


# class ResultCreateView(CreateView):
#     template_name = 'polytweets/result_form.html'
#     form_class = forms.ResultCreateForm
#     context_object_name = "context"
#
#     def get_object(self, queryset=None):
#         return super(ResultCreateView, self).get_object(queryset=queryset)
#
#     def get(self, request, *args, **kwargs):
#         return super(ResultCreateView, self).get(request, args, kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(ResultCreateView, self).get_context_data(**kwargs)
#
#         if self.request.method == 'GET':
#             pass
#
#         return context
#
#     def form_valid(self, form):
#         # As explained in the mptt documentation, the node needs to be inserted into a tree, if any,
#         # before the instance of the new object (here a Fragment) is save inside the DB. There are two ways
#         # to access the instance: form.instance or form.save(commit=False). It seems the second is preferable.
#         self.object = form.save(commit=False)
#         self.object.save()
#         return super(ResultCreateView, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy("index")
