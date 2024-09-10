from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        context = {
            'title': "Bosh sahifa",
        }
        return render(request, 'news/index.html', context)


class AboutView(View):
    def get(self, request):
        context = {
            'title': "Biz haqimizda",
        }
        return render(request, 'news/about.html', context)


class CategoryView(View):
    def get(self, request):
        context = {
            'title': "Kategoriyalar",
        }
        return render(request, 'news/category.html', context)


class LatestNewsView(View):
    def get(self, request):
        context = {
            'title': "So'ngi xabarlar",
        }
        return render(request, 'news/latest_news.html', context)


class BlogView(View):
    def get(self, request):
        context = {
            'title': "Blog",
        }
        return render(request, 'news/blog.html', context)


class BlogDetailsView(View):
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
