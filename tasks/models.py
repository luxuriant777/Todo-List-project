from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_at = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tags")

    class Meta:
        ordering = ["completed", "-created_at"]
