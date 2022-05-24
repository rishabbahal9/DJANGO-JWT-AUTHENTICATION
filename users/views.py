from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from users.serializers import UserSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
import jwt

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TestView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Test, Successful'}
        return Response(content)


class UserView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        try:
            access_token_obj = AccessToken(token)
            user_id = access_token_obj['user_id']
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Could not verify token\'s authenticity!')
        user = User.objects.filter(id=user_id).first()
        return Response({"id": user.id ,"first_name": user.first_name, "last_name": user.last_name, "username": user.username, "email": user.email})

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)