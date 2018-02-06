from django.db import models


__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        # +로 설정하면 역참조가 없어짐.
        related_name='+',
    )

    def __str__(self):
        return f'{self.name} (id: {self.pk})'

    @property
    def following(self):
        following_relations = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        following_pk_list = following_relations.values_list('to_user', flat=True)
        following_users = TwitterUser.objects.filter(pk__in=following_pk_list)
        return following_users

    @property
    def followers(self):
        pk_list = self.relations_by_to_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING
        ).values_list('from_user', flat=True)
        return TwitterUser.objects.filter(pk__in=pk_list)

    @property
    def block_users(self):
        pk_list = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_BLOCK.values_list('to_user', flat=True)
        )
        return TwitterUser.objects.filter(pk__in=pk_list)

    def is_followee(self, to_user):
        return self.following.filter(pk=to_user.pk).exists()

    def is_follower(self, to_user):
        pass

    def follow(self, to_user):
        self.relations_by_from_user.filter(to_user=to_user).delete()
        Relation.objects.create(
            from_user=self,
            to_user=to_user,
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        # 다른 방법
        # self.relations_by_from_user.create(
        #     to_user=to_user,
        #     type=Relation.RELATION_TYPE_FOLLOWING,
        # )

    def block(self, to_user):
        self.relations_by_from_user.filter(to_user=to_user).delete()
        self.relations_by_from_user.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_BLOCK,
        )


class Relation(models.Model):
    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 from_user 인 경우에 Relation 목록을 가져오고 싶을 경우
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 to_user 인 경우에 Relation 목록을 가져오고 싶을 경우
        related_name='relations_by_to_user',
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('from_user', 'to_user'),
        )
