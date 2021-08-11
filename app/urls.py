from django.urls import path
from app.views import CrudView, AlgorithmViews

urlpatterns = [
    path('data/', CrudView.as_view(), name='app-url-list'),
    path('data-detail/<str:pk>/', CrudView.as_view(), name="data-detail"),
    path('data-create/', CrudView.as_view(), name="data-create"),
    path('data-update/<str:pk>/', CrudView.as_view(), name="data-update"),
    path('data-delete/<str:pk>/', CrudView.as_view(), name="data-delete"),
    path('train/', AlgorithmViews.as_view(), name="train"),
    path('predict/', AlgorithmViews.as_view(), name="predict"),
    
]