from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'



# explication : 
#rest_framework.serializers : Module de Django REST Framework qui contient les outils pour créer des serializers.
#Un serializer permet de convertir des données complexes (comme des objets Django) en formats simples (JSON, XML, etc.) pour les API, et vice versa.
#Task : Modèle Task importé depuis les modèles de l'application pour être sérialisé.
#TaskSerializer : Cette classe définit un serializer pour le modèle Task.
#serializers.ModelSerializer : Une sous-classe spécialisée de Serializer qui génère automatiquement des champs en fonction des attributs du modèle.
#La classe interne Meta est utilisée pour configurer le serializer :

#model = Task : Indique que ce serializer est basé sur le modèle Task. Tous les champs définis dans le modèle Task seront utilisés dans ce serializer.
#fields = '__all__' : Inclut tous les champs du modèle Task dans le serializer.

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

# Classe UserSerializer :

#Hérite de serializers.ModelSerializer, ce qui permet de convertir un modèle Django en JSON et vice-versa.
#La gestion du mot de passe est effectuée à l'aide de serializers.CharField avec l'attribut write_only=True, ce qui empêche le mot de passe d'être renvoyé dans les réponses.
#Validation du mot de passe :

#Utilise validate_password pour valider les mots de passe en fonction des règles de sécurité de Django.
#Méthode create :

#Crée un utilisateur avec un mot de passe sécurisé grâce à set_password, ce qui hache le mot de passe avant de le sauvegarder.
#Méthode update :

#Permet de mettre à jour les attributs d'un utilisateur existant. Si un nouveau mot de passe est fourni, il est haché avant la sauvegarde.