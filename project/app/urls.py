from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path("registerparent/", views.customer_register, name="customer_register"),
    path("registerstaf/", views.seller_register, name="seller_register"),
    path("registeradmin/", views.admin_register, name="admin_register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path('parenthome',views.parenthome,name='parenthome'),
    path('stafhome',views.stafhome,name='stafhome'),
    path("addchild/", views.add_child, name="add_child"),
    path("viewchildren/", views.view_children, name="view_children"),
    path('adddailyactivity/', views.add_daily_activity, name='add_daily_activity'),
    path('listdailyactivity/', views.list_daily_activity, name='list_daily_activity'),


]
