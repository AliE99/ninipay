from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, ClothsViewSet, AccessoryViewSet

router = DefaultRouter()
router.register('foods', FoodViewSet)
router.register('cloths', ClothsViewSet)
router.register('accessories', AccessoryViewSet)

urlpatterns = router.urls
