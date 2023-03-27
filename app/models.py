from django.db import models

# Create your models here.
# blog
class Blog(models.Model):
    title = models.CharField('タイトル', max_length=255)
    content = models.TextField('内容')
    update_at = models.DateTimeField('更新日', auto_now=True)
    create_at = models.DateTimeField('作成日', auto_now_add=True)

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'

    def __str__(self) -> str:
        return self.title