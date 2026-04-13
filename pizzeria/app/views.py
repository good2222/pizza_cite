from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza, Category, Order, OrderItem
from .forms import OrderForm



def menu(request):
    categories = Category.objects.prefetch_related('pizzas').all()
    pizzas = Pizza.objects.filter(is_available=True).select_related('category')
    selected_cat = request.GET.get('category')
    if selected_cat:
        pizzas = pizzas.filter(category__slug=selected_cat)
    return render(request, 'menu.html', {
        'pizzas': pizzas,
        'categories': categories,
        'selected_cat': selected_cat,
    })


def pizza_detail(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk, is_available=True)
    return render(request, 'pizza_detail.html', {'pizza': pizza})


def order_create(request, pizza_pk):
    pizza = get_object_or_404(Pizza, pk=pizza_pk, is_available=True)
    size = request.GET.get('size', 'medium')
    price = pizza.get_price(size)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            size = request.POST.get('size', 'medium')
            quantity = int(request.POST.get('quantity', 1))
            price = pizza.get_price(size)
            order.total_price = price * quantity
            order.save()

            OrderItem.objects.create(
                order=order,
                pizza=pizza,
                size=size,
                quantity=quantity,
                price=price,
            )

            return redirect('order_list')
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {
        'form': form,
        'pizza': pizza,
        'size': size,
        'price': price,
    })


def order_list(request):
    orders = Order.objects.prefetch_related('items__pizza').all()
    return render(request, 'order_list.html', {'orders': orders})
