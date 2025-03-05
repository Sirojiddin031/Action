
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CourseViewSet, DayViewSet, RoomViewSet, TableTypeViewSet, TableViewSet,
                    GroupViewSet, TopicViewSet, GroupHomeworkViewSet, HomeworkViewSet)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'days', DayViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'tabletypes', TableTypeViewSet)
router.register(r'tables', TableViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'grouphomeworks', GroupHomeworkViewSet)
router.register(r'homeworks', HomeworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
