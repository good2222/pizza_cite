from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва категорії')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='Повне імʼя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, verbose_name='Email')),
                ('delivery_type', models.CharField(choices=[('delivery', 'Доставка'), ('pickup', 'Самовивіз')], default='delivery', max_length=10, verbose_name='Тип отримання')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адреса доставки')),
                ('notes', models.TextField(blank=True, verbose_name='Коментар до замовлення')),
                ('status', models.CharField(choices=[('new', 'Новий'), ('confirmed', 'Підтверджено'), ('cooking', 'Готується'), ('delivery', 'В доставці'), ('done', 'Виконано'), ('cancelled', 'Скасовано')], default='new', max_length=10, verbose_name='Статус')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сума замовлення')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('ingredients', models.TextField(blank=True, verbose_name='Склад')),
                ('price_small', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ціна маленька')),
                ('price_medium', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ціна середня')),
                ('price_large', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ціна велика')),
                ('price_xl', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ціна XL')),
                ('is_spicy', models.BooleanField(default=False, verbose_name='Гостра')),
                ('is_vegetarian', models.BooleanField(default=False, verbose_name='Вегетаріанська')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступна')),
                ('is_new', models.BooleanField(default=False, verbose_name='Новинка')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pizzas', to='app.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Піца',
                'verbose_name_plural': 'Піци',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('small', 'Маленька'), ('medium', 'Середня'), ('large', 'Велика'), ('xl', 'XL')], default='medium', max_length=10, verbose_name='Розмір')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Кількість')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ціна за шт.')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.order', verbose_name='Замовлення')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app.pizza', verbose_name='Піца')),
            ],
            options={
                'verbose_name': 'Позиція замовлення',
                'verbose_name_plural': 'Позиції замовлення',
            },
        ),
    ]
