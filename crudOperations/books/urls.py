from django.urls import path
from .views import *
urlpatterns = [
    path('',Bookslist),
    path('add/',Create_book),
    path('update/<int:id>/',Update_book),
    path('delete/<int:id>/',Delete_book),

]