from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='user_img', null=True)

    def __unicode__(self):
        return "{}".format(self.username)


class Post(models.Model):
    user = models.ForeignKey(User, related_name="post_users")
    title = models.CharField(max_length=60)
    url = models.CharField(max_length=140)
    description = models.CharField(max_length=140)

    def __unicode__(self):
        return "{}".format(self.title)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comment_users")
    post = models.ForeignKey(Post, related_name="comment_posts")
    content = models.CharField(max_length=10000)

    def __unicode__(self):
        return "Comment on {} from {}".format(
            self.post.title,
            self.user.username,
        )


class Vote(models.Model):
    user = models.ForeignKey(User, related_name='vote_users')
    post = models.ForeignKey(Post, related_name='vote_posts')

    def __unicode__(self):
        return "Upvote for {} from {}".format(
            self.post.title,
            self.user.username,
        )