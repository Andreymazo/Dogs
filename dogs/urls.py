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
    # path('dogs/', DogViewSet.as_view({'get': 'list', 'post': 'create'}), name='dogs'),
    path('dogs/0', BreedListView.as_view(), name='dogs'),
    path('dogs/create', BreedCreateView.as_view(), name='dogs2'),
    path('dogs/<int:pk>', BreedUpdateView.as_view(), name='dog3'),
    path('dogs/<int:pk>', BreedRetrieveView.as_view(), name='dogs4'),
    path('dogs/4', BreedRetrieveUpdateDestroy.as_view(), name='dogs5')
              ] + router.urls
# urlpatterns = [
#     path('', include(router.urls)),
# ]
