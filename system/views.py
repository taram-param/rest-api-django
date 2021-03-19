from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Fundraising, Fee
from .serializers import FundraisingSerializer, FeeSerializer


class AllFundraisingView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        fundraisings = Fundraising.objects.filter(participants__username__icontains=request.user.username)
        serializer = FundraisingSerializer(fundraisings, many=True)

        return Response({
            "Все сборы": serializer.data
        })


class FundraisingDetailView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        fundraising = get_object_or_404(Fundraising.objects.all(), pk=pk)
        fundraising_serializer = FundraisingSerializer(fundraising, many=False)
        fee = Fee.objects.filter(fundraising=fundraising)
        fee_serializer = FeeSerializer(fee, many=True)

        return Response({
            "Сбор": fundraising_serializer.data,
            "Сдавшие": fee_serializer.data
        })
