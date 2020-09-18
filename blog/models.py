from django.db import models
import uuid
from .search import PostIndex
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', null=True)
    post_id = models.CharField(max_length=255, null=False, default=uuid.uuid4().__str__())
    is_active = models.BooleanField(default=True)
    content = models.TextField(null=True)
    title = models.TextField(null=True)

    # Method for indexing the model
    def indexing(self):
        obj = PostIndex(
            meta={'id': self.id},
            author=self.author.username,
            created_at=self.created_at,
            title=self.title,
            text=self.content
        )
        obj.save()
        return obj.to_dict(include_meta=True)

