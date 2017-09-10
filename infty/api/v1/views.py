from rest_framework import viewsets, generics, views

from infty.core.models import Topic, Comment, CommentSnapshot, Transaction
from infty.api.v1.serializers import *

from rest_framework import viewsets, mixins
from rest_framework import filters


class CustomViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()` and `list()` actions.
    We don't use `destroy()` yet.
    """
    pass

class TopicViewSet(CustomViewSet):

    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(CustomViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TransactionViewSet(CustomViewSet):

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


