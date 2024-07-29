from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, MemberCreateView, MemberUpdateView, MemberDeleteView

router = DefaultRouter()
router.register(r'members', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('members/create/', MemberCreateView.as_view(), name='member-create'),
    path('members/update/<int:pk>/', MemberUpdateView.as_view(), name='member-update'),
    path('members/delete/<int:pk>/', MemberDeleteView.as_view(), name='member-delete'),
]