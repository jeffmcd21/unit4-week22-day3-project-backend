
from .models import Team_Info
from .models import Batter_Info
from rest_framework import viewsets, permissions
from .serializers import TeamSerializer, BatterSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset=Team_Info.objects.all().order_by('id')
    serializer_class=TeamSerializer
    permission_classes=[permissions.AllowAny]

class BatterViewSet(viewsets.ModelViewSet):
    queryset=Batter_Info.objects.all().order_by('id')
    serializer_class=BatterSerializer
    permission_classes=[permissions.AllowAny]

