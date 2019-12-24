from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from blog.models import Post

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'date_posted',
            'content',
        ]

class PostListSerializer(ModelSerializer):
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'date_posted',
        ]

    def get_author(self, obj):
        return str(obj.author.username)

class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'date_posted',
            'content',
        ]


    def get_author(self, obj):
        return str(obj.author.username)
