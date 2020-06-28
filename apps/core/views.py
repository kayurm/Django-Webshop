from django.shortcuts import render, get_object_or_404

from apps.core.models import Category, Product, Tag


def index(request):
    context = {}
    category_qs = Category.objects.all().order_by('-popularity')[:5]
    product_qs = Product.objects.order_by('-title')[:3]
    context['category_list'] = category_qs
    context['product_list'] = product_qs
    return render(request, 'core/index.html', context)


def category_list(request):
    context = {}
    category_qs = Category.objects.all()
    context['category_list'] = category_qs
    return render(request, 'core/category_list.html', context)


def category_detail(request, slug):
    context = {}
    # category = Category.objects.filter(slug=slug).first()
    category = get_object_or_404(Category, slug=slug)
    context['category'] = category
    return render(request, 'core/category.html', context)


# - отображать только те товары, что есть в наличии
# - товары должны быть отсортированы по дате последнего изменения
def product_list(request):
    context = {}
    product_qs = Product.objects.filter(in_stock=True).order_by('-updated_at')
    context['product_list'] = product_qs
    return render(request, 'core/product_list.html', context)


def product_detail(request, slug_category, pk):
    context = {}
    product = Product.objects.filter(
        pk=pk, category__slug=slug_category
    ).first()
    context['product'] = product
    return render(request, 'core/product.html', context)
