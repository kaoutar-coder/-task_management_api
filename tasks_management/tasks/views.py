

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer    #indique que le TaskSerializer sera utilisé pour sérialiser et désérialiser les données des tâches.
    permission_classes = [IsAuthenticated] #Restreint l'accès aux utilisateurs authentifiés uniquement. Si un utilisateur non authentifié tente d'accéder à une route, une erreur HTTP 401 (Unauthorized) sera renvoyée


    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

        # Cette méthode retourne l'ensemble de données à utiliser pour cette vue.
        #Ici, elle est surchargée pour filtrer les tâches appartenant uniquement à l'utilisateur connecté (self.request.user).#Cela garantit que chaque utilisateur ne voit que ses propres tâches.
        


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        # Cette méthode est appelée lors de la création d'une tâche
        #Ajoute automatiquement l'utilisateur connecté (self.request.user) comme propriétaire (owner) de la nouvelle tâche.Cela empêche les utilisateurs de créer des tâches sans être associés à elles






#explication :
# rest_framework.viewsets :
#Contient la classe ModelViewSet, une abstraction qui combine les actions CRUD (Create, Read, Update, Delete) et les mixins de DRF.
#rest_framework.permissions.IsAuthenticated :
#Une classe de permissions qui limite l'accès aux utilisateurs authentifiés.
#Task : Le modèle de tâche à manipuler.
#TaskSerializer : Le serializer utilisé pour convertir les objets Task en données JSON et vice versa.
#TaskViewSet :
#TaskViewSet :
#Définit un ensemble de vues pour gérer les opérations CRUD sur le modèle Task.
#Hérite de ModelViewSet, ce qui permet d'accéder automatiquement aux actions suivantes :
#Lister (list) : Affiche toutes les tâches disponibles.
#Créer (create) : Ajoute une nouvelle tâche.
#Récupérer (retrieve) : Récupère une tâche spécifique.
#Mettre à jour (update/partial_update) : Modifie une tâche existante.
#Supprimer (destroy) : Supprime une tâche.





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








#
#
#
#
#
