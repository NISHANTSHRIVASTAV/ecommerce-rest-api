from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.Serializers):

    class Meta:
        model = Category
        fields = ('name', 'description')
