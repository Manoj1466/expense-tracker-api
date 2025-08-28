from django.urls import path 
from . import views

urlpatterns = [
    path('',views.indexpage,name='index_page'),
    path('register/', views.register_user,name='register_page'),
    path('login/',views.login_user,name='login_page'),
    path('logout/',views.logout_user,name='logouturl'),
    path('main/',views.maniPage, name='main_page'),
    path('expense/',views.expense, name='expense_page'),
    path('showcase/',views.showcase_expenses, name='showcase_page'),
    path('expense/delete/<int:expense_id>/',views.delete_expense,name='delete_expense'),
]
