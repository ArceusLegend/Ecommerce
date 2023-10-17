from django.shortcuts import get_object_or_404, render

from . import models


def categories(request):
    return {"categories": models.Category.objects.all()}


def all_products(request):
    products = models.Product.objects.all()
    return render(request, "store/home.html", {"products": products})


def product_detail(request, slug):
    product = get_object_or_404(models.Product, slug=slug, in_stock=True)
    return render(request, "store/products/detail.html", {"product": product})


def category_list(request, category_slug=None):
    category = get_object_or_404(models.Category, slug=category_slug)
    products = models.Product.objects.filter(category=category)
    return render(request, "store/products/categories.html", {"category": category, "products": products})
