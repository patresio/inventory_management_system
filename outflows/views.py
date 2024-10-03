from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from outflows.forms import OutflowForm
from outflows.models import Outflow
from utils.metrics import get_sales_metrics


class OutflowListView(LoginRequiredMixin, ListView):
    model = Outflow
    template_name = "outflow_list.html"
    context_object_name = "outflows"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sales_metrics"] = get_sales_metrics
        return context


class OutflowCreateView(LoginRequiredMixin, CreateView):
    model = Outflow
    template_name = "outflow_create.html"
    form_class = OutflowForm
    success_url = reverse_lazy("outflows:list")


class OutflowDetailView(LoginRequiredMixin, DetailView):
    model = Outflow
    template_name = "outflow_detail.html"
    context_object_name = "outflow"
