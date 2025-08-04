from rest_framework import viewsets
from .models import BillGroup, BillGroupMember, Bill
from .serializers import BillGroupDetailSerializer, BillGroupSerializer, BillGroupMemberSerializer, BillSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class BillGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return BillGroup.objects.filter(user=self.request.user)

    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BillGroupDetailSerializer
        return BillGroupSerializer


class BillGroupMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BillGroupMemberSerializer

    def get_queryset(self):
        return BillGroupMember.objects.filter(bill_group__user=self.request.user)

class BillViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BillSerializer

    def get_queryset(self):
        return Bill.objects.filter(bill_group__user=self.request.user)