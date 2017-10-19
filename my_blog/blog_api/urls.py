from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = router.urls
