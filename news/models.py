from django.db import models


class News(models.Model):
    title = models.CharField(max_length=511)
    author = models.CharField(max_length=255, null=True)
    description = models.TextField()

    content = models.TextField()
    url = models.URLField()
    url_to_image = models.URLField(null=True)
    published_at = models.DateTimeField()

    source_id = models.CharField(max_length=255, null=True)
    source_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "News"
        unique_together = ["title", "source_name"]
        ordering = ["-published_at"]
