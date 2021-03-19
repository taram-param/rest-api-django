from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Fundraising, Fee


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()

    class Meta:
        model = User


class FundraisingSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=500)
    opening_date = serializers.DateTimeField()
    closing_date = serializers.DateTimeField()
    participants = UserSerializer(many=True, read_only=True)
    amount = serializers.IntegerField()

    class Meta:
        model = Fundraising


class FeeSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    user = UserSerializer(many=False, read_only=True)
    date = serializers.DateTimeField()
    amount = serializers.IntegerField()

    class Meta:
        model = Fee

