from django.urls import path
from.import views

urlpatterns =[
    path('reg',views.register,name='reg'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]