from django.shortcuts import render, get_object_or_404
from .models import Category,Product
# Create your views here.


def index(request,template_name):
    page_title="产品主页"
    return render(request,template_name,locals())

def show_category(request,template_name,category_slug):
    c=get_object_or_404(Category, slug=category_slug,is_active=True)
    products = c.product_set.all()
    page_title=c.name
    meta_keywords=c.meta_keywords
    meta_description = c.meta_description
    return  render(request,template_name,locals())


def show_product(request,template_name,product_slug):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title=p.name
    meta_keywords=p.meta_keywords
    meta_description = p.meta_description
    return  render(request,template_name,locals())