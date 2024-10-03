from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from categories.forms import CategoryForm
from categories.models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "category_create.html"
    form_class = CategoryForm
    success_url = reverse_lazy("categories:list")


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "category_detail.html"
    context_object_name = "category"


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "category_update.html"
    form_class = CategoryForm
    success_url = reverse_lazy("categories:list")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "category_delete.html"
    success_url = reverse_lazy("categories:list")
