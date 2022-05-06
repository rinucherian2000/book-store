from django.forms import ModelForm
from owner.models import Books
from django import forms
from customer.models import Orders


class Bookform(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
            "images Q5R": forms.FileInput(attrs={"class": "form-control"}),
        }
        # exclude=("active_status",)

class OrderProcessform(ModelForm):
    class Meta:
        model=Orders
        fields=["status","expected_delivery_date"]
        widgets={
            "status":forms.Select(attrs={"class":"form-control"}),
            "expected_delivery_date":forms.DateInput(attrs={"class":"form-control","type":"date"})

        }

