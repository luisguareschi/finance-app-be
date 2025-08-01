from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillGroupViewSet, BillGroupMemberViewSet, BillViewSet

router = DefaultRouter()
router.register(r'bill-groups', BillGroupViewSet, basename='bill-groups')
router.register(r'bill-group-members', BillGroupMemberViewSet, basename='bill-group-members')
router.register(r'bills', BillViewSet, basename='bills')

urlpatterns = [
    path('', include(router.urls)),
]