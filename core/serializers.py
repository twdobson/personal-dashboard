from rest_framework import serializers, viewsets
from rest_framework import permissions
from apps.polls.models import Passenger

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passenger
        fields = ['name', 'sex', 'survived']

# ViewSets define the view behavior.
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]