

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    id = models.AutoField(primary_key=True)  # Add ID field
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title


#explication models : django.db.models :
#  Contient les classes de base pour définir des modèles dans Django.
#django.contrib.auth.models.User : Représente le modèle utilisateur intégré de Django, qui permet de gérer les utilisateurs (authentification, permissions, etc.).
#Task : Représente un modèle de tâche. Chaque instance de cette classe correspond à une ligne dans une table de base de données.
#CharField : Champ de type texte de taille fixe.
#TextField : Champ pour un texte long.
#blank=True : Permet que le champ soit vide lors de la saisie dans un formulaire.
#null=True : Permet que la valeur soit NULL dans la base de données.
#BooleanField : Champ qui prend deux valeurs possibles : True (vrai) ou False (faux).
#default=False : La tâche est considérée comme "non terminée" par défaut.
#DateTimeField : Champ pour stocker une date et une heure.
#auto_now_add=True : Remplit automatiquement ce champ avec la date et l'heure actuelles lors de la création de la tâche.
#auto_now=True : Met à jour automatiquement ce champ à chaque fois que la tâche est modifiée.
#ForeignKey : Définit une relation de clé étrangère (une tâche appartient à un utilisateur).
#User : Le propriétaire est lié au modèle User de Django.
#on_delete=models.CASCADE : Si un utilisateur est supprimé, toutes ses tâches seront supprimées également.
#