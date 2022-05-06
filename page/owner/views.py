from django.shortcuts import render, redirect
from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView, DetailView
from owner.forms import Bookform
from owner.models import Books
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from customer.decorators import owner_permission_required
from customer.models import Orders
from owner.forms import OrderProcessform
from django.core.mail import send_mail



# Create your views here.
@method_decorator(owner_permission_required,name='dispatch')

class BookList(ListView):
    model = Books
    context_object_name = "item"
    template_name = "avail_books.html"
    # def get(self, request, *args, **kwargs):
    #     books = Books.objects.all()
    #     context = {"item": books}
    #     return render(request, "avail_books.html", context)

@method_decorator(owner_permission_required,name='dispatch')
class AddBooks(CreateView):
    model = Books
    form_class = Bookform
    template_name = "book_add.html"
    success_url = reverse_lazy('listbook')

    # def get(self, request, *args, **kwargs):
    #     form = Bookform()
    #     context = {"item": form}
    #     return render(request, "book_add.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     book = Bookform(request.POST,files=request.FILES)
    #     if book.is_valid():
    #         book.save()
    #         # bookname = book.cleaned_data.get("book_name")
    #         # author = book.cleaned_data.get("author")
    #         # price = book.cleaned_data.get("price")
    #         # copies = book.cleaned_data.get("copies")
    #         # book = Books(book_name=bookname, author=author, price=price, copies=copies)
    #         # book.save()
    #         return redirect("listbook")

@method_decorator(owner_permission_required,name='dispatch')
class BookDetail(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "book_detail.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listbook')
    # def get(self, request, *args, **kwargs):
    #     id = kwargs["id"]
    #     det = Books.objects.get(id=id)
    #     # book=[book for book in books if book["id"]==id][0] #this 0 eliminates the list and moves it to a dictionary
    #     context = {"book": det}
    #     return render(request, "book_detail.html", context)

@method_decorator(owner_permission_required,name='dispatch')

class Bookchange(UpdateView):
    model = Books
    form_class = Bookform
    template_name = "bookedit.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listbook')
    # def get(self, request, *args, **kwargs):
    #     id = kwargs["id"]
    #     edit = Books.objects.get(id=id)
    #     # dict = {"book_name": edit.book_name,
    #     #         "author": edit.author,
    #     #         "price": edit.price,
    #     #         "copies": edit.copies
    #     #         }
    #     form = Bookform(instance=edit)
    #     context = {"item": form}
    #     return render(request, "bookedit.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     id = kwargs["id"]
    #     edit = Books.objects.get(id=id)
    #     form = Bookform(request.POST, instance=edit, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("listbook")

    # book=[book for book in books if book["id"]==id][0]
    # form=Bookform(initial={"Book_name":book["book_name"],"Author":book["author"],"Price":book["price"],"Copies":book["copies"]})
    # form=Bookform(initial=book)
    # return render(request,"bookedit.html",{"form":form})

@method_decorator(owner_permission_required,name='dispatch')
class Bookdelete(DeleteView):
    model = Books
    template_name = 'bookdelete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listbook")
    # def get(self, request, *args, **kwargs):
    #     id = kwargs["id"]
    #     dele = Books.objects.get(id=id)
    #     dele.delete()
    #     return redirect("listbook")



class OwnerDashBoard(ListView):
    model = Orders
    template_name = "dashboard.html"
    def get(self,request,*args,**kwargs):
        new_order=self.model.objects.filter(status="orderplaced")
        context={"orders":new_order}
        return render(request,self.template_name,context)

class OwnerOrders(DetailView):
    model = Orders
    template_name = "viewdetail.html"
    pk_url_kwarg = "id"
    context_object_name ="order"

class OrderProcessView(UpdateView):
    model = Orders
    template_name = "orderprocess.html"
    pk_url_kwarg = "id"
    form_class =OrderProcessform
    success_url = reverse_lazy("dashborad")
    def form_valid(self, form):
        self.object=form.save()
        expected_delivery_date=form.cleaned_data.get("expected_delivery_date")
        send_mail(
            'Book Order Conformation',
            'Your Order Will Be Delivered On'+str(expected_delivery_date),
            'rinucherian2000@gmail.com',
            ['akhilmohan04869@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)





