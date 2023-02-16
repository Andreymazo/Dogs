from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.urls import path

from config import settings
from dogs.apps import DogsConfig
from dogs.views import DogViewSet, BreedListView, BreedCreateView, BreedRetrieveView, BreedUpdateView, \
    BreedRetrieveUpdateDestroy
 # SigninView, SignupView,
app_name = DogsConfig.name
router = DefaultRouter()
router.register(r'dogs', DogViewSet, basename='dogs')

urlpatterns = [
    path('dogs/', BreedListView.as_view(), name='dogs'),
    path('dogs/1', BreedCreateView.as_view(), name='dogs2'),
    path('dogs/2', BreedUpdateView.as_view(), name='dog3'),
    path('dogs/3', BreedRetrieveView.as_view(), name='dogs4'),
    path('dogs/4', BreedRetrieveUpdateDestroy.as_view(), name='dogs5')
              ] + router.urls
# urlpatterns = [
#     path('', include(router.urls)),
# ]
