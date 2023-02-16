from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView

from dogs.models import Dog, Breed
from rest_framework import viewsets, generics

from dogs.serializer import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()

class BreedListView(ListAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()

class BreedCreateView(CreateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()

class BreedUpdateView(UpdateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()

class BreedRetrieveView(RetrieveAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
class BreedRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()



