from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, mixins
from base.models import Post
from base.serializers import PostSerializer
from .mixins import UserQuerysetMixin, StaffEditorPermissionMixin


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ Customize Token Serializer """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    """ Generic view to retrieve single row of data """
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostListAPIView(generics.ListAPIView):
    """Generic view to retrieve a collection of data (Not in use) """
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostCreateAPIView(generics.CreateAPIView, StaffEditorPermissionMixin, UserQuerysetMixin):
    """ Generic view to create single row of data (Not in use) """
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    def perform_create(self, serializer):
        """
        Overwrite the build in perform_create function to ajust the create view
        """
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        # Optional: Send django signal after save function
        serializer.save(user=self.request.user, content=content)

class PostUpdateAPIView(generics.UpdateAPIView, StaffEditorPermissionMixin, UserQuerysetMixin):
    """ Generic view to update single row of data """
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field='pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        return super().perform_update(instance)

class PostDestroyAPIView(generics.DestroyAPIView, StaffEditorPermissionMixin, UserQuerysetMixin):
    """ Generic view to delete single row of data """
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field='pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)