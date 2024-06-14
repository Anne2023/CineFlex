from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Movie, Rental
from .serializers import UserSerializer, MovieSerializer, RentalSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request):
        movies = self.queryset
        return render(request, 'movie_list.html', {'movies': movies})

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
