
from rest_framework.routers import DefaultRouter
from auth_views import Auth

router = DefaultRouter()

# Register the ViewSet with the router
router.register(r'auth', Auth, basename='auth')

urlpatterns = router.urls
