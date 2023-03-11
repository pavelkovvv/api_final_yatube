import json

from django.shortcuts import get_object_or_404

from posts.models import User


def user_str_to_user_pk(request):
    """Функция для преобразования поля из типа str (мы получаем
    от пользователя) в тип int (нужен, чтобы мы могли сохранить
    значение в БД)
    """
    data = json.loads(request.body)
    following_str = data['following']
    following = get_object_or_404(User, username=following_str)
    print(following.pk)
    return following.pk
