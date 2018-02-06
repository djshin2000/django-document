from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

    def __str__(self):
        # 출력 결과 >> 이한영 (친구: 박보영, 아이유)

        # list comprehensions 사용
        return '{name} (친구: {friends})'.format(
            name=self.name,
            friends=', '.join([friend.name for friend in self.friends.all()])
        )

        # Manager 의 value_list 사용
        # return '{name} (친구: {friends})'.format(
        #     name=self.name,
        #     friends=', '.join(self.friends.value_list('name', flat=True))
        # )
