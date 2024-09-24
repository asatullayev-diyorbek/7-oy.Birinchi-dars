from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name="Nom")
    slug = models.SlugField(max_length=30, verbose_name="Slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kategorilar"
        verbose_name = "Kategiriya"

    def last_news(self):
        return News.objects.filter(category=self, is_published=True).order_by('-created_at').first()

    def first_news(self):
        return News.objects.filter(category=self, is_published=True).order_by('created_at').first()


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    title = models.CharField(max_length=200, verbose_name="Nom")
    slug = models.SlugField(max_length=200, verbose_name="Slug")
    content = RichTextField(verbose_name="Kontent")
    views = models.PositiveIntegerField(default=0, verbose_name="Ko'rilishlar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shildi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilandi")
    image = models.ImageField(upload_to="news/images/", verbose_name="Rasm")
    is_published = models.BooleanField(default=True, verbose_name="Ko'rinishi")
    author = models.CharField(max_length=50, verbose_name="Yozuvchi")
    quotes = models.TextField(verbose_name="Iqtibos")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Yangiliklar"
        verbose_name = "Yangilik"

    def get_image(self):
        if self.image:
            return self.image.url
        return "https://t4.ftcdn.net/jpg/04/70/29/97/360_F_470299797_UD0eoVMMSUbHCcNJCdv2t8B2g1GVqYgs.jpg"


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Yangilik")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    content = models.TextField(verbose_name="Komentariya")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shildi")

    def __str__(self):
        return f"{self.user.username} - {self.news.title}"

    class Meta:
        verbose_name_plural = "Komentariyalar"
        verbose_name = "Komentariya"
