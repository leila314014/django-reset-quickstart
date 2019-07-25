"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
# from rest_framework.authtoken.views import ObtainAuthToken

from django.conf.urls.static import static
from core.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

from categories.views import CategoryViewSet
from comments.views import CommentViewSet
from posts.views import PostViewSet
from users.views import UserViesSet

router = DefaultRouter(False)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)
router.register('posts', PostViewSet)
router.register('users', UserViesSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('token/', ObtainAuthToken.as_view()),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(
        title='Django Rest Quick Start Docs',
        authentication_classes=[SessionAuthentication],
        permission_classes=[IsAdminUser],
    )),
]

# 顯示superuser_image
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
