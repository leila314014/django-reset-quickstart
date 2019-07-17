from rest_framework import serializers

from comments.serializers import CommentSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['creator']  # 排除這個欄位
        read_only_fields = ['create_at']


class PostCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        exclude = ['creator']
        read_only_fields = ['create_at']
