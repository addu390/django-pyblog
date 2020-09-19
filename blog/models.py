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

    class Meta:
        db_table = "post"
        indexes = [
            models.Index(fields=['updated_at'], name='post_created_at_idx'),
        ]
        unique_together = [['post_id']]

    def indexing(self):
        obj = PostIndex(
            meta={'id': self.id},
            author=self.author.username,
            post_id=self.post_id,
            is_active=self.is_active,
            title=self.title,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
        obj.save()
        return obj.to_dict(include_meta=True)

