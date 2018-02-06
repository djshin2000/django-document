from django.contrib import admin

from .models import (Pizza, Topping, Post, User, PostLike, FacebookUser)

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
admin.site.register(FacebookUser)
