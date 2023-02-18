from django.db import models


class News(models.Model):
    author = models.CharField(max_length=255, null=True)
    title = models.TextField()
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return f"({self.author}) {self.title}"
