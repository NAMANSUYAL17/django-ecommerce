from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ProductForm
from django.shortcuts import render,redirect
from .models import Product,Category
app_name='products'
def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(is_available=True)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 2)  # 6 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': category,
        'categories': categories,
        'page_obj': page_obj,
    }

    return render(request, 'products/product_list.html', context)
# Create your views here.
def product_detail(request, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
        is_available=True
    )

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)
@login_required
@user_passes_test(lambda u: u.is_staff)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()

    return render(request, 'products/product_form.html', {'form': form})