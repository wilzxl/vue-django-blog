from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # "all" will use all paragraph
        fields = '__all__'
