"""test_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pages import views


router = DefaultRouter()
router.register('pages', views.PageModelViewset)
router.register('content_videos', views.VideoModelViewset)
router.register('content_audios', views.AudioModelViewset)
router.register('content_texts', views.TextModelViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/', include('pages.urls')),
]

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]
