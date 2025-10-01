from rest_framework import serializers
from .models import Dentist, Contact
from django.contrib.auth.models import User


class Dentist_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = "__all__"


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class Contact_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
