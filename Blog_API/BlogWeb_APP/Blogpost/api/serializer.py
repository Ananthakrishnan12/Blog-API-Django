from rest_framework import serializers
from Blogpost.models import blogpost,Comment


class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogpost
        fields = "__all__"
        
        
class CommentSerializer(serializers.ModelSerializer):
    comment_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comment
        fields="__all__"