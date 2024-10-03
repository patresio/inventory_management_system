from django import forms
from django.core.exceptions import ValidationError

from outflows.models import Outflow


class OutflowForm(forms.ModelForm):

    class Meta:
        model = Outflow
        fields = ["product", "quantity", "description"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        product = self.cleaned_data.get("product")

        if quantity > product.quantity:
            raise ValidationError(
                f"A quantidade disponível em estoque do {product.title} é de {product.quantity}. Por favor, informe uma quantidade menor."
            )
        return quantity
