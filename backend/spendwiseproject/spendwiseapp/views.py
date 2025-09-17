ffrom rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import RegisterSerializer
from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer

class RegisterView(APIView):
    permission_classes=[AllowAny]

    def post(self,request):
        serializer= RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user=serializer.save()
            if user:
                refresh=RefreshToken.for_user(user)
                return Response({
                    "user":user.username,
                   " refresh":str(refresh),
                   "access": str(refresh.access_token),
                },status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset=Category.objects.all()
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 



class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Expense.objects.all()

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LoginView(TokenObtainPairView):
    permission_classes=[AllowAny]        


class RefreshToken(TokenRefreshView):
    permission_class=[AllowAny]

