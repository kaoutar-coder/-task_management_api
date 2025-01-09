
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer    
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        

#Ajouter une vue pour gérer les utilisateurs

from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Les utilisateurs peuvent uniquement gérer leur propre compte
        return User.objects.filter(id=self.request.user.id)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Authentification de l'utilisateur
    user = authenticate(request, username=username, password=password)
    if user:
        # Créer un token de rafraîchissement et un token d'accès
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'message': 'Login successful!',
            'access_token': access_token
        })
    else:
        return Response({'message': 'Incorrect username or password'}, status=400)
