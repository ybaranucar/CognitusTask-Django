from django.urls import path

from . import views

urlpatterns = [
    path('', views.url_list, name='app-url-list'),
    path('data/', views.get_data_list, name="data-list"),
    path('data-detail/<str:pk>/', views.get_data_detail, name="data-detail"),  
	path('data-create/', views.data_create, name="data-create"),
    path('data-update/<str:pk>/', views.data_update, name="data-update"),
	path('data-delete/<str:pk>/', views.data_delete, name="data-delete"),
    path('train/', views.get_train, name="train"),
    path('predict/', views.post_predict, name="predict"),
]