from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
# Create your views here.

def productlist(request, category_slug=None):
    category = None
    productlist = Product.objects.get_queryset().order_by('id')
    category_list = Category.objects.annotate(total_products=Count('product'))
    
    # category filter
    if category_slug :
        category =get_object_or_404(Category, slug=category_slug)
        productlist = productlist.filter(category=category)

    # search filter
    search_query = request.GET.get('q')
    if search_query :
        productlist = productlist.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(condition__icontains = search_query) |
            Q(brand__brand_name__icontains = search_query)
        )

    # pagination
    paginator = Paginator(productlist,1)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    template = 'Product/product_list.html'
    context = { 
        'product_list' : productlist, 
        'category_list' : category_list,
        'category' : category}
    return  render(request, template, context)

def productdetail(request,product_slug):
    productdetail =get_object_or_404(Product, slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    context = { 'product_detail' : productdetail , 'product_images' : productimages }
    template = 'Product/product_detail.html'
    return  render(request, template, context)