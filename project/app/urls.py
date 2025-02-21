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
    path("edit_child/<int:child_id>/", views.edit_child_details, name="edit_child"),
    path("add_fee/", views.add_fee_transaction, name="add_fee"),
    path("view_fees/",views. view_fees, name="view_fees"),
    path("viewchildren/", views.view_children, name="view_children"),
    path('adddailyactivity/', views.add_daily_activity, name='add_daily_activity'),
    path('listdailyactivity/', views.list_daily_activity, name='list_daily_activity'),

    path('about/',views.about,name='name'),
    path("children/",views.child_list, name="child_list"),
    path("child/<int:child_id>/fees/", views.child_fee_details, name="child_fee_details"),
    path("child/<int:child_id>/pay/", views.process_payment, name="process_payment"),
    path("child/<int:child_id>/payment-success/", views.payment_success, name="payment_success"),
    
    path('adminhome',views.adminhome,name='adminhome'),
    path('viewparents',views.viewparents,name='viewparents'),
    path('viewfeedetails',views.viewfeedetails,name='viewfeedetails'),
    path('viewstaf',views.viewstaf,name='viewstaf'),
    path('dailyactivities',views.dailyactivities,name='dailyactivities'),





]
