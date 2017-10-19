from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ArticleViewSet, LoginView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = router.urls
urlpatterns.append(url(r'^auth/login$', LoginView.as_view()))
