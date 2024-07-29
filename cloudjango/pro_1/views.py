
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Member
from .serializers import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberCreateView(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberUpdateView(UpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDeleteView(DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
