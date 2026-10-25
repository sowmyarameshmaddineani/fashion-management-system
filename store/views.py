from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Category, CartItem, Address, Order

def index(request):
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')
    
    products = Product.objects.all()
    
    if category_slug:
        products = products.filter(category__slug=category_slug)
    if search_query:
        products = products.filter(title__icontains=search_query)

    categories = Category.objects.all()
    
    context = {
        'products': products[:48],
        'categories': categories,
        'selected_category': category_slug
    }
    return render(request, 'store/index.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'login_form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile_view(request):
    if request.method == 'POST':
        Address.objects.create(
            user=request.user,
            full_name=request.POST['full_name'],
            street_address=request.POST['street_address'],
            city=request.POST['city'],
            state=request.POST['state'],
            pincode=request.POST['pincode'],
            phone=request.POST['phone']
        )
        return redirect('profile')
    
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'store/profile.html', {'addresses': addresses})

@login_required
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect('cart')
    
    total = sum(item.total_price() for item in cart_items)
    addresses = Address.objects.filter(user=request.user)

    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        if address_id:
            address = get_object_or_404(Address, id=address_id, user=request.user)
            # Create the Order using the 'address' foreign key
            order = Order.objects.create(
                user=request.user,
                address=address,
                total_amount=total,
                status='Pending'
            )
            cart_items.delete()
            return render(request, 'store/order_success.html', {'order': order})
            
    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total': total, 'addresses': addresses})

@login_required
def orders_view(request):
    user_orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/orders.html', {'orders': user_orders})