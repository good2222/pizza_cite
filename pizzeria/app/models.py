from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва категорії')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Pizza(models.Model):
    SIZE_CHOICES = [
        ('small', 'Маленька 25см'),
        ('medium', 'Середня 30см'),
        ('large', 'Велика 35см'),
        ('xl', 'XL 40см'),
    ]

    name = models.CharField(max_length=100, verbose_name='Назва')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pizzas',
        verbose_name='Категорія'
    )
    description = models.TextField(blank=True, verbose_name='Опис')
    ingredients = models.TextField(blank=True, verbose_name='Склад')
    image_url = models.URLField(blank=True, verbose_name='Фото (URL)')
    price_small = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна маленька')
    price_medium = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна середня')
    price_large = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна велика')
    price_xl = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна XL')
    is_spicy = models.BooleanField(default=False, verbose_name='Гостра')
    is_vegetarian = models.BooleanField(default=False, verbose_name='Вегетаріанська')
    is_available = models.BooleanField(default=True, verbose_name='Доступна')
    is_new = models.BooleanField(default=False, verbose_name='Новинка')

    class Meta:
        verbose_name = 'Піца'
        verbose_name_plural = 'Піци'

    def __str__(self):
        return self.name

    def get_price(self, size='medium'):
        prices = {
            'small': self.price_small,
            'medium': self.price_medium,
            'large': self.price_large,
            'xl': self.price_xl,
        }
        return prices.get(size, self.price_medium)


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новий'),
        ('confirmed', 'Підтверджено'),
        ('cooking', 'Готується'),
        ('delivery', 'В доставці'),
        ('done', 'Виконано'),
        ('cancelled', 'Скасовано'),
    ]

    DELIVERY_CHOICES = [
        ('delivery', 'Доставка'),
        ('pickup', 'Самовивіз'),
    ]

    full_name = models.CharField(max_length=150, verbose_name='Повне імʼя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Email')
    delivery_type = models.CharField(
        max_length=10,
        choices=DELIVERY_CHOICES,
        default='delivery',
        verbose_name='Тип отримання'
    )
    address = models.CharField(max_length=255, blank=True, verbose_name='Адреса доставки')
    notes = models.TextField(blank=True, verbose_name='Коментар до замовлення')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сума замовлення')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
        ordering = ['-created_at']

    def __str__(self):
        return f'Замовлення #{self.pk} — {self.full_name}'

    def calc_total(self):
        return sum(item.subtotal() for item in self.items.all())


class OrderItem(models.Model):
    SIZE_CHOICES = [
        ('small', 'Маленька'),
        ('medium', 'Середня'),
        ('large', 'Велика'),
        ('xl', 'XL'),
    ]

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Замовлення'
    )
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name='Піца'
    )
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='medium', verbose_name='Розмір')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кількість')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна за шт.')

    class Meta:
        verbose_name = 'Позиція замовлення'
        verbose_name_plural = 'Позиції замовлення'

    def __str__(self):
        return f'{self.pizza.name} ({self.size}) x{self.quantity}'

    def subtotal(self):
        return self.price * self.quantity
