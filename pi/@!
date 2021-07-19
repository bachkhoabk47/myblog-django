from django.views import generic
from django.shortcuts import render
from django.db.models import Q
from . import models
from .models import Post
from about.models import About
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.views import generic

from . import forms

def home(request):
    list_recent_article = Post.objects.all().order_by('-created')[:5]
    list_home_article = Post.objects.filter(publish=True)
    list_article = Post.objects.filter(publish=True)
    list_category = Category.objects.all()
    category = request.GET.get('category')

    query = request.GET.get("q")
    if query:
        list_article = list_article.filter(
            Q(title__icontains=query)|
            Q(body__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()

        paginator = Paginator(list_article, 4) # Show 25 contacts per pagepaginator = Paginator(contact_list, 25) # Show 25 contacts per page
        list_category = Category.objects.all()

        page = request.GET.get('page')
        try:
            list_article = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            list_article = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            list_article = paginator.page(paginator.num_pages)   

        def next_page_number(self):
            return self.paginator.validate_number(self.number + 1)

        def previous_page_number(self):
            return self.paginator.validate_number(self.number - 1)
        return render(request, "posts_in_category.html", {"list_article":list_article, "list_recent_article":list_recent_article, "list_category":list_category})

    if category:
        list_article = list_article.filter(category__slug__icontains=category)
        paginator = Paginator(list_article, 4) # Show 25 contacts per pagepaginator = Paginator(contact_list, 25) # Show 25 contacts per page
        list_category = Category.objects.all()

        page = request.GET.get('page')
        try:
            list_article = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            list_article = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            list_article = paginator.page(paginator.num_pages)   

        def next_page_number(self):
            return self.paginator.validate_number(self.number + 1)

        def previous_page_number(self):
            return self.paginator.validate_number(self.number - 1)
        return render(request, "posts_in_category.html", {"list_article":list_article, "list_recent_article":list_recent_article, "list_category":list_category})
    

    paginator = Paginator(list_home_article, 4) # Show 25 contacts per pagepaginator = Paginator(contact_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        list_home_article = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_home_article = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list_home_article = paginator.page(paginator.num_pages)

    def next_page_number(self):
        return self.paginator.validate_number(self.number + 1)

    def previous_page_number(self):
        return self.paginator.validate_number(self.number - 1)

    return render(request, "home.html", {"list_article":list_article , "list_home_article":list_home_article, "list_recent_article":list_recent_article, "list_category":list_category})

def post_detail(request, category_slug, post_slug):
   #list_recent_article = Post.objects.all()[:5]
   list_recent_article = Post.objects.all().order_by('-created')[:5]
   Category.objects.filter(slug=category_slug)
   post = get_object_or_404(Post, slug = post_slug)
   list_category = Category.objects.all()
   return render(request, 'post_detail.html', {'post': post, "list_recent_article":list_recent_article, 'list_category':list_category})

def contact(request):
    list_category = Category.objects.all()
    list_recent_article = Post.objects.all().order_by('-created')[:5]
    #list_recent_article = Post.objects.all()[:5]
    return render(request, 'contact.html', {"list_recent_article":list_recent_article, 'list_category':list_category})

def about(request):
    #list_recent_article = Post.objects.all()[:5]
    list_recent_article = Post.objects.all().order_by('-created')[:5]
    list_category = Category.objects.all()
    list_about = About.objects.all()
    return render(request, 'about.html', {'list_about': list_about,"list_recent_article":list_recent_article, 'list_category':list_category})

def album(request):
    return render(request, 'album.html')

def htmlspecialchars(text):
    return (
        text.replace("&", "&amp;").
        replace('"', "&quot;").
        replace("<", "&lt;").
        replace(">", "&gt;")
    )


class CkEditorFormView(generic.FormView):
    form_class = forms.CkEditorForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('ckeditor-form')

ckeditor_form_view = CkEditorFormView.as_view()
