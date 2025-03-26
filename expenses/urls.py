from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ExpenseViewSet, CategoryViewSet, RegisterView

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]