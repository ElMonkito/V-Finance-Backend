from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, CategoryViewSet, RegisterView
from django.urls import path, include

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]
