from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name="Nom")
    slug = models.SlugField(max_length=30, verbose_name="Slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kategorilar"
        verbose_name = "Kategiriya"


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    title = models.CharField(max_length=200, verbose_name="Nom")
    slug = models.SlugField(max_length=200, verbose_name="Slug")
    content = models.TextField(verbose_name="Kontent")
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
