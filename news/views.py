from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Prefetch
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Category, Comment


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        categories_with_news = Category.objects.prefetch_related(
            Prefetch('news_set', queryset=News.objects.filter(is_published=True))
        )
        trending_newses = News.objects.filter(is_published=True).order_by('-views')[:2]
        newses = News.objects.filter(is_published=True).order_by('-created_at')[:10]
        most_newses =  News.objects.filter(is_published=True).order_by('-views')[:5]
        context = {
            'title': "Bosh sahifa",
            'categories': categories_with_news,
            'trending_newses': trending_newses,
            'newses': newses,
            'most_newses': most_newses,
        }
        return render(request, 'news/index.html', context)


class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'title': "Biz haqimizda",
        }
        return render(request, 'news/about.html', context)


class CategoryView(LoginRequiredMixin, View):
    def get(self, request):
        categories_with_news = Category.objects.prefetch_related(
            Prefetch('news_set', queryset=News.objects.filter(is_published=True))
        )
        context = {
            'title': "Kategoriyalar",
            'categories': categories_with_news,
        }
        return render(request, 'news/category.html', context)


class LatestNewsView(LoginRequiredMixin, View):
    def get(self, request, slug):
        news = News.objects.filter(slug=slug).first()

        context = {
            'title': "So'ngi xabarlar",
            'news': news,
        }
        return render(request, 'news/latest_news.html', context)


class CommentView(LoginRequiredMixin, View):
    def post(self, request):
        news_id = request.POST.get('news_id')
        content = request.POST.get('content')
        if news_id and content:
            news = News.objects.filter(id=news_id).first()
            if news:
                Comment.objects.create(news=news, user=request.user, content=content)
                messages.success(request, "Komentariya qo'shildi!")
            else:
                messages.error(request, "Yangilik topilmadi!")
        else:
            messages.error(request, "Iltimos komentari kiriting!")
        page = request.META.get('HTTP_REFERER', 'news:category')
        return redirect(page)

    def get(self, request):
        return redirect('news:category')


class BlogView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'title': "Blog",
        }
        return render(request, 'news/blog.html', context)


class BlogDetailsView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'title': "Blog qismi",
        }
        return render(request, 'news/blog_details.html', context)


class ContactView(View):
    def get(self, request):
        context = {
            'title': "Bog'lanish",
        }
        return render(request, 'news/contact.html', context)
