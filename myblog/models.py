from django.db import models
from django.utils import timezone


class BlogComment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    approved_comment = models.BooleanField()
    post = models.ForeignKey('Post', models.DO_NOTHING, related_name='comments')
    #  The related_name option in models.ForeignKey allows us to have access to comments from within the Post model.
    
    class Meta:
        managed = False
        db_table = 'blog_comment'

    def __str__(self):
        return 'Commento di: ' + self.author

    def approve (self):
        self.approved_comment = True
        self.save()


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
	

    class Meta:
        managed = False
        db_table = 'post'

    def __str__(self):
        return 'Post di: ' + str(self.author) + ' ' + self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


