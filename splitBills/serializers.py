from rest_framework import serializers
from .models import BillGroup, BillGroupMember, Bill

class BillGroupSerializer(serializers.ModelSerializer):
    number_of_members = serializers.SerializerMethodField()
    class Meta:
        model = BillGroup
        fields = (
            "id",
            "name",
            "number_of_members",
            "created_at",
            "updated_at",
            "currency",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "number_of_members",
        )

    def get_number_of_members(self, obj):
        return obj.number_of_members

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class BillGroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillGroupMember
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = (
            'id',
            'bill_group',
            'payed_by',
            'description',
            'amount',
            'payed_for',
            'payed_for_everyone',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )

class BillDetailSerializer(serializers.ModelSerializer):
    payed_for = BillGroupMemberSerializer(many=True)
    payed_by = BillGroupMemberSerializer()
    class Meta:
        model = Bill
        fields = (
            'id',
            'bill_group',
            'payed_by',
            'description',
            'amount',
            'payed_for',
            'payed_for_everyone',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('id', 'created_at', 'updated_at')


class BillGroupDetailSerializer(BillGroupSerializer):
    bill_group_members = BillGroupMemberSerializer(many=True)   
    bills = BillDetailSerializer(many=True)
    class Meta(BillGroupSerializer.Meta):
        fields = BillGroupSerializer.Meta.fields + ('bill_group_members', 'bills')
        read_only_fields = BillGroupSerializer.Meta.read_only_fields + ('bill_group_members', 'bills')