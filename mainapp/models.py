from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название новости')
    content = models.TextField()
    url_article = models.URLField(max_length=300) # url для ссылки новости
    url_photo = models.URLField(max_length=300, blank=True, null=True)   #url для ссылки фотографии

    def __str__(self):
        return self.title


