from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')  # Ajoutez les routes pour les utilisateurs

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
]




#django.urls.path :
#Permet de définir les chemins URL de l'application.
#django.urls.include :
#Utilisé pour inclure les routes générées par le routeur DRF.
#rest_framework.routers.DefaultRouter :
#Un routeur fourni par Django REST Framework qui génère automatiquement les routes pour les ViewSets.
#Prend en charge les actions standards des ViewSets (list, retrieve, create, update, delete, etc.).
#TaskViewSet :
#Le ViewSet défini dans le fichier views.py, qui gère les opérations CRUD pour les tâches.
#DefaultRouter :
#Un routeur DRF qui génère automatiquement des routes RESTful pour les ViewSets.
#Exemple : /tasks/, /tasks/<id>/, etc.
#register :
#Permet d’enregistrer un ViewSet auprès du routeur.
#Premier argument (r'tasks') :
#Le préfixe des routes, ici : tasks.
#Deuxième argument (TaskViewSet) :
#Le ViewSet à utiliser pour ces routes.
#basename :
#Une base pour nommer les routes. Ici, toutes les routes générées seront basées sur le nom task.