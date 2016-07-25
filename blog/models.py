from django.conf import settings
from django.core.urlresolvers import reverse
from category.models import Category

from django.db import models
from django.db.models.signals import pre_save
from django.utils.encoding import smart_str

from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    id_sort = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, unique=True)
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=255, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, null=True)
    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title.encode('utf8')

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-id_sort"]
        
class Album(models.Model):
    title = models.CharField(max_length=255, unique=True)
    publish = models.BooleanField(default=True)
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title.encode('utf8')

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
