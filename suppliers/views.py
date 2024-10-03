from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from suppliers.forms import SupplierForm
from suppliers.models import Supplier


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    template_name = "supplier_create.html"
    form_class = SupplierForm
    success_url = reverse_lazy("suppliers:list")


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = "supplier_detail.html"
    context_object_name = "supplier"


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    template_name = "supplier_update.html"
    form_class = SupplierForm
    success_url = reverse_lazy("suppliers:list")


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "supplier_delete.html"
    success_url = reverse_lazy("suppliers:list")
