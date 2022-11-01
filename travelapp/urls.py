from django.urls import path
from.import views
urlpatterns = [
    path('',views.fun,name='fun'),
    path('',views.nun,name='nun'),
    # path('add',views.addittion,name='add')
]
