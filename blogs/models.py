from django.db import models


class BlogPost(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    date_added = models.DateTimeField("Дата добавления", auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title
