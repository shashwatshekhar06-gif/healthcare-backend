from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'patients', views.PatientViewSet, basename='patient')
router.register(r'doctors', views.DoctorViewSet, basename='doctor')

urlpatterns = [
    path('auth/register/', views.RegisterView.as_view()),
    path('auth/login/', views.LoginView.as_view()),
    path('mappings/', views.MappingListCreateView.as_view()),
    path('mappings/<int:pk>/', views.MappingDetailView.as_view()),
    path('', include(router.urls)),
]
