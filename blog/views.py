from django.views import generic
from django.shortcuts import render
from django.db.models import Q
from . import models
from models import Post
from about.models import About
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.views import generic

from . import forms

def home(request):
    #queryset_list = Post.objects.active()
    #list_article = Post.objects.all()
    list_article = Post.objects.filter(publish=True)
    query = request.GET.get("q")
    if query:
      list_article = list_article.filter(
        Q(title__icontains=query)|
        Q(body__icontains=query)
        ).distinct()

    #for article in list_article:
    #    if article.publish:
    #        list_article = Post.objects.filter(publish__icontains=article.publish)



    category = request.GET.get('category')
    print category

    if category:
      list_article = list_article.filter(category__slug__icontains=category)

    paginator = Paginator(list_article, 2) # Show 25 contacts per pagepaginator = Paginator(contact_list, 25) # Show 25 contacts per page
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

    return render(request, "index.html",{"list_article":list_article, "list_category":list_category})

def post_detail(request, category_slug, post_slug):
   #category = get_object_or_404(Category, id = category_id)
   #category = get_object_or_404(Category, slug = category_slug)
   Category.objects.filter(slug=category_slug)
   post = get_object_or_404(Post, slug = post_slug)
   list_category = Category.objects.all()
   #post = Post.objects.get(pk=post_id)
   #category = Category.objects.get(pk=category_id)
   return render(request, 'post_detail.html', {'post': post, 'list_category':list_category})

def contact(request):
    list_category = Category.objects.all()
    return render(request, 'contact.html', {'list_category':list_category})

def about(request):
    list_category = Category.objects.all()
    list_about = About.objects.all()
    return render(request, 'about.html', {'list_about': list_about, 'list_category':list_category})

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
