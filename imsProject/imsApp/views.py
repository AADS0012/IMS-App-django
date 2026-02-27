from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product

# ------------------------

# params: user request
# return: (show) the first view of app
def home_view(req):
    return render(req, 'imsApp/index.html')

# params: user request
# - desc :
#          -show the create product form view &&
#          -validation form. if valid: then save product and redirect
#          -else: reload and show error
# return: redirect into the product list page || reload view
def product_create_view(req):
    form = ProductForm()
    if req.method == 'POST':
        form = ProductForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(req,'imsApp/productForm.html', {'form': form})

# params: user request
# - desc :
#          -get all of products and show it
# return: (show) the products list view app
def products_list_view(req):
    products = Product.objects.all()
    return render(
        req,
        'imsApp/productsList.html',
        {'products': products})

# params: user request
# - desc :
#          -get the product data and show a product
#          -view. if valid: then save product and redirect
#          -else: reload and show error
# return: redirect into the product list page || reload view
def products_update_view(req, product_id):
    product = Product.objects.get(product_id= product_id)
    form = ProductForm(instance=product)
    if req.method == 'POST':
        form = ProductForm(req.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(req,'imsApp/productForm.html', {'form': form})

# params: user request
# - desc :
#          -get the product data and confirm user for
#          -delete the product if method is post
#          -else: reload
# return: redirect into the product list page || reload view
def product_delete_view(req, product_id):
    product = Product.objects.get(product_id= product_id)
    if req.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(req, 'imsApp/productConfirmDelete.html')