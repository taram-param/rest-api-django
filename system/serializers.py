from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=120)
    age = serializers.IntegerField()
    address = serializers.CharField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.age = validated_data.get("age", instance.age)
        instance.address = validated_data.get("address", instance.address)

        instance.save()
        return instance
