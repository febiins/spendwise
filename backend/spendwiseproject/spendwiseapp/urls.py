from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RegisterView,CategoryViewSet,ExpenseViewSet,LoginView,RefreshToken

router= DefaultRouter()

router.register(r'categories',CategoryViewSet,basename='category')
router.register(r'expenses',ExpenseViewSet,basename='expense')

urlpatterns=[
    path("register/",RegisterView.as_view(),name='register'),
    path("login/",LoginView.as_view(),name='login'),
    path("token/refersh/",RefreshToken.as_view(),name='token_refresh'),
    path("",include(router.urls))
]