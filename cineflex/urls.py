from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import UserViewSet, MovieViewSet, RentalViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'rentals', RentalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('movies/', MovieViewSet.as_view({'get': 'list'}), name='movie-list'),
]
