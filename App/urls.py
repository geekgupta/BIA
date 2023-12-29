from django.urls import path
from .views import DashboardPage  , BookList , BookDetail , ModifyVideo


app_name = 'App'  # Add name of the app 

urlpatterns = [
    path('' , DashboardPage , name="dashbaord"), ## task 1 
    path('api/books/', BookList.as_view(), name='book-list'), ## task 2
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book-detail'),  ## task 3 
    path('modify_video/', ModifyVideo.as_view(), name='modify_video'), ## task 5

]
