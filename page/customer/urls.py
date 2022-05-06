from django.urls import path
from customer import  views

urlpatterns=[
    # path('home',views.index),
    # path("carts",views.view_my_cart),
    # path('orders',views.view_my_order),
    # path('feedback',views.FeedBackView.as_view()),
    # path('registration',views.RegistrationView.as_view()),
    # path("/login", views.Loginview.as_view(), name="login"),
    path("home",views.CustomerHome.as_view(),name="home"),
    path("signup",views.SignUpView.as_view(),name="signup"),
    path("signin",views.SignInView.as_view(),name="signin"),
    path("signout",views.SignOut,name="signout"),
    path("customer/cart/add/<int:id>",views.AddToCart.as_view(),name="addtocart"),
    path("customer/cart/view",views.CartView.as_view(),name="viewcart"),
    path("customer/cart/remove/<int:id>",views.RemoveCart.as_view(),name="removed"),
    path("customer/cart/orders/<int:p_id>/<int:c_id>",views.OrderView.as_view(),name="orders"),
    path("customer/myorder",views.MyOrderView.as_view(),name="myorder"),
    path("customer/cancel/<int:o_id>",views.cancel_view,name="cancel"),
    path("customer/profile",views.ProfileView.as_view(),name="profie"),
    path("customer/view/profile",views.ViewProfile.as_view(),name="viewprofile"),

    # path("customer/carts/add/<int:id>",views.Addtocartview.as_view(),name="addtocart ")

]