from django.conf.urls  import url
from . import views
urlpatterns = [
    url(r'^category/(?P<category_slug>[-\w]+)/$',views.show_category,
    {'template_name':"catalog/category.html"},name='catelog_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$',views.show_product,
    {'template_name':"catalog/product.html"},name='catelog_product'),
]