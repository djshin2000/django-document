from datetime import datetime
from django.utils import timezone
from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        # MTM 으로 연결된 반대편에서 자동 생성되는 역방향 매니저 이름인
        # post_set 대신 like_posts 라는 이름을 사용하도록 한다.
        related_name='like_posts'
    )

    def __str__(self):
        return self.title


# Extra fields on many-to-many relationships
class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{post}의 좋아요.({user}, {created_date})'.format(
            post=self.post,
            user=self.user,
            created_date=datetime.strftime(
                # timezone.make_naive(self.created_date), '%y.%m.%d'
                timezone.localtime(self.created_date), '%y.%m.%d'
            )
        )
