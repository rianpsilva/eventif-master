from django.db import models


class Speaker(models.Model):
    name = models.CharField('Nome',max_length=255)
    slug = models.SlugField('Slug')
    photo = models.URLField('Foto')
    website = models.URLField('Website', blank=True)
    description = models.TextField('Descrição', blank= True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name
# Create your models here.
