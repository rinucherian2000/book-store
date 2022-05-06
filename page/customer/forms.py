from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import ModelForm
from customer.models import Orders
from customer.models import Profile




class UserRegisterationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=["address"]
        widgets={
            "address": forms.Textarea(attrs={"class": "form-control"}),

        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["address","phone_no","profile_pic"]
        widgets={
            "address":forms.Textarea(attrs={"class":"form-control"}),
            "phone_no": forms.NumberInput(attrs={"class": "form-control"}),
            "profile_pic": forms.FileInput(attrs={"class": "form-control"}),
        }

































































# class FeedBackForm(forms.Form):
#     product_name=forms.CharField()
#     feedback=forms.CharField()
#
# class RegistrationFrom(forms.Form):
#     first_name=forms.CharField()
#     last_name=forms.CharField()
#     phone=forms.CharField()
#     email=forms.CharField()
#     username=forms.CharField
#     password=forms.CharField(widget=forms.PasswordInput())
#
#     def clean(self):
#         cleaned_data = super().clean()
#         phone = cleaned_data.get("phone")
#         print(phone)
#         if len(phone) != 10:
#             message = "invalid number"
#             self.add_error("phone", message)
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
#     password = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
