from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=256, unique = True ,)

    def __str__(self):
        return self.name

class Article(models.Model):

    

    title = models.CharField(max_length=256, verbose_name='Название',)
    text = models.TextField(verbose_name='Текст',)
    published_at = models.DateTimeField(verbose_name='Дата публикации',)
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Tag,through = 'Scope', related_name='scopes',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


    

class Scope(models.Model):

    article = models.ForeignKey(Article, on_delete = models.CASCADE,related_name='aricles_tag', )
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE,related_name='aricles_tag', )
    is_main = models.BooleanField()
    
    def __str__(self):
        return f'{self.is_main}'



    

