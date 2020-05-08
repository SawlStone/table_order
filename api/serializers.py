from rest_framework import serializers

from main.models import TableOrder


class TableOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOrder
        fields = '__all__'

    def create(self, validated_data):
        return TableOrder.objects.create(**validated_data)
