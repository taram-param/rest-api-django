from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Person
from .serializers import PersonSerializer


class AllPersonView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)

        return Response({"people": serializer.data})

    def post(self, request):
        person = request.data.get("person")
        serializer = PersonSerializer(data=person)

        if serializer.is_valid(raise_exception=True):
            person_saved = serializer.save()

        return Response({
            "success": "Person '{}' created successfully".format(person_saved.title)
        })


class PersonView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        person = get_object_or_404(Person.objects.all(), pk=pk)
        serializer = PersonSerializer(person, many=False)

        return Response({
            "person": serializer.data
        })

    def put(self, request, pk):
        saved_person = get_object_or_404(Person.objects.all(), pk=pk)
        data = request.data.get("person")
        serializer = PersonSerializer(instance=saved_person, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            person_saved = serializer.save()

        return Response({
            "success": "Person '{}' updated successfully".format(person_saved.title)
        })

    def delete(self, request, pk):
        person = get_object_or_404(Person.objects.all(), pk=pk)
        person.delete()

        return Response({
            "message": "Person '{}' deleted successfully".format(pk)
        }, status=204)
