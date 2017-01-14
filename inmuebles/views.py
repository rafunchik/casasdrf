from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, DjangoFilterBackend
from inmuebles.filters import InmuebleFilter

from inmuebles.models import Inmueble
from inmuebles.permissions import IsOwnerOrReadOnly
from inmuebles.serializers import InmuebleSerializer, UserSerializer




class InmuebleViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code inmuebles.

    The **owner** of the code inmueble may update or delete instances
    of the code inmueble.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter, )
    filter_class = InmuebleFilter
    search_fields = ('descripcion', 'extras')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of inmueble instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer