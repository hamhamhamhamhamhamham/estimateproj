from rest_framework import generics
# new
from rest_framework.permissions import IsAdminUser
from .models import Estimate
from .serializers import EstimateSerializer


class EstimateCreateView(generics.CreateAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes=[IsAdminUser]

class EstimateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes=[IsAdminUser]



