from rest_framework import serializers

from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.shortcuts import get_object_or_404

from posts.models import Comment, Post, Follow, User, Group


class SearchFollow(serializers.Field):
    """Класс для преобразования поля из типа str (мы получаем
    от пользователя) в тип int (нужен, чтобы мы могли сохранить
    значение в БД)
    """

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        following = get_object_or_404(User, username=data)
        return following


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'created', 'post')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = SearchFollow()

    class Meta:
        fields = ('user', 'following')
        model = Follow
        read_only_fields = ('user',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'))
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['following'] = instance.following.username
        ret['user'] = instance.user.username
        return ret
