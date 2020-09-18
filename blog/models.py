from django.db import models
import uuid


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    user_id = models.CharField(max_length=255, null=False)
    post_id = models.CharField(max_length=255, null=False, default=uuid.uuid4().__str__())
    is_active = models.BooleanField(default=True)
    content = models.TextField(null=True)
    title = models.TextField(null=True)

    class Meta:
        db_table = "post"
        indexes = [
            models.Index(fields=['post_id'], name='post_idx'),
        ]
        unique_together = [['post_id', 'is_active']]

    def __str__(self):
        return self.name


class Tag(BaseModel):
    post_id = models.CharField(max_length=255, null=False)
    tag_id = models.CharField(max_length=255, null=False, default=uuid.uuid4().__str__())
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255, null=False)
    title = models.TextField(null=True)

    class Meta:
        db_table = "tags"
        indexes = [
            models.Index(fields=['post_id'], name='post_tag_idx'),
        ]
        unique_together = [['post_id', 'tag_id']]

    def __str__(self):
        return self.name
