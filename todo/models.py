from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["completed", "created"]

    def __str__(self) -> str:
        return f"{self.content}"
