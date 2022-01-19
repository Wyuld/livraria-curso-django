from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = routers.DefaultRouter()
router.register(r"categorias-viewset", views.CategoriaViewSet)
router.register(r"editoras", views.EditoraViewSet)
router.register(r"autores", views.AutorViewSet)
router.register(r"livros", views.LivroViewSet)
router.register(r"compras", views.CompraViewSet)

urlpatterns = [
    # path('teste/', views.test),
    # path('teste2/', views.test2),
    # Outros Endpoints
    path("admin/", admin.site.urls),
    path("categorias-class/", views.CategoriaView.as_view()),
    path("categorias-class/<int:id>/", views.CategoriaView.as_view()),
    path("categorias-apiview/", views.CategoriasList.as_view()),
    path("categorias-apiview/<int:id>/", views.CategoriaDetail.as_view()),
    path("categorias-generic/", views.CategoriasListGeneric.as_view()),
    path("categorias-generic/<int:id>/", views.CategoriasDetailGeneric.as_view()),
    path("api/", include(router.urls)),
    # Autenticação
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # OpenAPI3 (DRF Spectacular)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
