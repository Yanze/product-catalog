from django.shortcuts import render, redirect
from .models import Product
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView



class Index(ListView):
    model = Product
    template_name = "catalog/index.html"


class CreateProduct(CreateView):
    model = Product
    fields = ['brand', 'name', 'price', 'description']
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        return super(CreateProduct, self).form_valid(form)


class UpdateProduct(UpdateView):
    model = Product
    fields = ['brand', 'name', 'price', 'description']
    success_url = reverse_lazy('index')


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('index')
