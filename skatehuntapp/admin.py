from django.contrib import admin
from skatehuntapp.models import User, Comment, Post, Vote

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Vote)