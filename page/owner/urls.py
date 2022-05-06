from django.urls import path
from owner import views

urlpatterns = [
    path("books/all",views.BookList.as_view(),name="listbook"),
    path("books/add", views.AddBooks.as_view(), name="bookcreate"),
    path("books/change/<int:id>", views.Bookchange.as_view(), name="bookchange"),
    path("books/details/<int:id>",views.BookDetail.as_view(),name="bookdetail"),
    path("books/delete/<int:id>",views.Bookdelete.as_view(),name="bookdelete"),
    path("dashboard",views.OwnerDashBoard.as_view(),name="dashborad"),
    path("view/detail/<int:id>",views.OwnerOrders.as_view(),name="viewdetail"),
    path("order/process/update/<int:id>",views.OrderProcessView.as_view(),name="process")



]
