from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from users.serializers import UserSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
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
