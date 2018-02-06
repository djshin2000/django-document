from django.db import models


class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        # +로 설정하면 역참조가 없어짐.
        related_name='+',
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
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
