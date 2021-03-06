from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'mentors', views.MentorViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'mentorships', views.MentorshipViewset)
urlpatterns = [
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls',
                                                   namespace='rest_framework'))
]
