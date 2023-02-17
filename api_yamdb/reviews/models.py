from django.db import models
from users.models import User

from .validators import validate_year

LIMIT_TEXT = 15


class Category(models.Model):
    """Category type of work"""
    name = models.CharField(max_length=256, verbose_name="Название категории")
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Слаг категории",
        db_index=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Genre of work"""
    name = models.CharField(max_length=256, verbose_name="Название жанра")
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Слаг жанра",
        db_index=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='titles'
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles'
    )
    name = models.CharField(
        max_length=256,
        verbose_name="Название произведения",
        db_index=True)
    year = models.IntegerField(
        verbose_name="Дата выхода",
        validators=[validate_year],
        db_index=True)
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст отзыва")
    score = models.SmallIntegerField(default=1, verbose_name="Оценка")
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации отзыва",
        db_index=True)

    class Meta:
        ordering = ['-pub_date']
        unique_together = ('title', 'author')

    def __str__(self):
        return self.text[:LIMIT_TEXT]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст отзыва")
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации отзыва",
        db_index=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:LIMIT_TEXT]
