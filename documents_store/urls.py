from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from digital_docs.views import TopicViewSet, FolderViewSet, DocumentViewSet


router = DefaultRouter()

router.register('documents', DocumentViewSet, basename='documents')
router.register('folders', FolderViewSet, basename='folders')
router.register('topics', TopicViewSet, basename='topics')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
