from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View,ListView,CreateView,UpdateView,TemplateView
from owner.models import Books
from customer.forms import UserRegisterationForm
from customer.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from customer.decorators import sign_in_require
from django.utils.decorators import method_decorator
from django.db.models import Sum

from customer.models import Carts
from customer.models import Orders

from customer.forms import OrderForm
from customer.models import Profile
from customer.forms import ProfileForm
from django.urls import reverse_lazy


# Create your views here.

# def index(request):
# #     return HttpResponse('<h1> welcome to customer </h1>')
# #
# def view_my_cart(request):
#     return HttpResponse("< h1> customer carts </h1>")
#
#
# def view_my_order(request):
#     return HttpResponse("<h1> customer order </h1>")


# class FeedBackView(View):
#     def get(self, request):
#         form = FeedBackForm()
#         context = {"form": form}
#         return render(request, "add_feedback.html", context)
#
#     def post(self, request):
#         form = FeedBackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return render(request, "add_feedback.html")
#
#
# class RegistrationView(View):
#     def get(self, request):
#         form = RegistrationFrom()
#         context = {"form": form}
#         return render(request, "registraion.html", context)
#
#     def post(self, request):
#         form = RegistrationFrom(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return render(request, 'registraion.html')
#
#
# class Loginview(View):
#     def get(self, request, *args, **kwargs):
#         form = LoginForm()
#         context = {"form": form}
#         return render(request, "registraion.html")
#
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # return render(request,"login.html")
#             return redirect("login")  # This is the redirect method
#         else:
#             context = {"form": form}
#             return render(request, "login.html", context)




class SignUpView(View):
    def get(self,request):
        form=UserRegisterationForm()
        context={"form":form}
        return render(request,"signup.html",context)
    def post(self,request):
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "signup.html")
        else:
            context = {"form": form}
            return render(request, "signin.html", context)

class SignInView(View):
    def get(self,request):
        form=LoginForm()
        context={"form":form}
        return render(request,"signin.html",context)
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user= authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser:
                    return redirect("listbook")
                else:
                    return redirect("home")
            else:
                context = {"form": form}
                return render(request, "signin.html", context)


def SignOut(request):
        logout(request)
        return redirect("signin")

@method_decorator(sign_in_require,name='dispatch')
class CustomerHome(View):
    def get(self,request,*args,**kwargs):
        book=Books.objects.all()
        context = {"book": book}
        return render(request, "cust_index.html", context)


class AddToCart(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=Books.objects.get(id=id)
        user=request.user
        cart=Carts(item=book,user=user)
        cart.save()
        print("Add To Cart")
        return redirect("home")

class CartView(ListView):
    model = Carts
    template_name ="cart_item.html"
    context_object_name = "items"
    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user)
    def get(self,request,*args,**kwargs):
        logged_user=self.model.objects.filter(user=self.request.user,status="incart")
        total_sum=logged_user.aggregate(Sum("item__price"))
        total=total_sum["item__price__sum"]
        context={"items":logged_user,"total":total}
        return render(request,self.template_name,context)

class RemoveCart(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        cart=Carts.objects.get(id=id)
        cart.status="cancel"
        cart.save()
        return redirect("viewcart")

class OrderView(CreateView):
    model = Orders
    template_name = "customer_orders.html"
    form_class = OrderForm

    def post(self,request, *args, **kwargs):
        p_id=kwargs.get("p_id")
        c_id=kwargs.get("c_id")
        form=OrderForm(request.POST)
        if form.is_valid():
            book=Books.objects.get(id=p_id)
            cart=Carts.objects.get(id=c_id)
            user=request.user
            address=form.cleaned_data.get("address")
            order=Orders(user=user,item=book,address=address)
            order.save()
            cart.status="order_placed"
            cart.save()
            return redirect("home")

class MyOrderView(ListView):
    model = Orders
    template_name = "orderview.html"
    context_object_name = "orders"
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).exclude(status="cancel")

def cancel_view(request,*args,**kwargs):
    id=kwargs["o_id"]
    cart=Orders.objects.get(id=id)
    cart.status="cancel"
    cart.save()
    return redirect("myorder")

class ProfileView(CreateView):
    model = Profile
    template_name = "customerprofile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("home")
    def post(self,request):
        form=self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect("home")
        else:
            return redirect(request,self.template_name,{"form":form})


class ViewProfile(TemplateView):
    template_name = "myprofile.html"

















