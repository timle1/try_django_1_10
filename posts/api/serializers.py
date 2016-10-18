from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'content',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish'
        ]


"""

from posts.models import Post
from posts.api.serializers import PostSerializer
obj = Post.objects.first()
print(obj)

obj_data = PostSerializer(obj)
obj_data.data

data5 = {
    "title": "Yeahh buddy",
    "content": "New content",
    "publish": "2016-2-12",
    "slug": "yeah-buddy",

}
new_item = PostSerializer(data=data5)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


#session2

from posts.models import Post
from posts.api.serializers import PostDetailSerializer
data = {
    "title": "Yeahh buddy",
    "content": "New content",
    "publish": "2016-2-12",
    "slug": "yeah-buddy",

}

obj = Post.objects.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

"""