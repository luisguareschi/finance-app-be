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
        fields = '__all__'


class BillGroupDetailSerializer(BillGroupSerializer):
    bill_group_members = BillGroupMemberSerializer(many=True)
    class Meta(BillGroupSerializer.Meta):
        fields = BillGroupSerializer.Meta.fields + ('bill_group_members',)
        read_only_fields = BillGroupSerializer.Meta.read_only_fields + ('bill_group_members',)