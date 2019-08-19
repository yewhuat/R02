from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import ProfileSerializer

from ..models import Profile


class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
