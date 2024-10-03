from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from inflows.forms import InflowForm
from inflows.models import Inflow


class InflowListView(LoginRequiredMixin, ListView):
    model = Inflow
    template_name = "inflow_list.html"
    context_object_name = "inflows"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class InflowCreateView(LoginRequiredMixin, CreateView):
    model = Inflow
    template_name = "inflow_create.html"
    form_class = InflowForm
    success_url = reverse_lazy("inflows:list")


class InflowDetailView(LoginRequiredMixin, DetailView):
    model = Inflow
    template_name = "inflow_detail.html"
    context_object_name = "inflow"
