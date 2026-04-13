from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'email', 'delivery_type', 'address', 'notes']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Іван Петренко'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+380 XX XXX XX XX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'delivery_type': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'вул. Шевченка, 1, кв. 5'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Без цибулі, зателефонуйте за 10 хвилин...'}),
        }
        labels = {
            'full_name': "Повне ім'я",
            'phone': 'Телефон',
            'email': 'Email (необовʼязково)',
            'delivery_type': 'Спосіб отримання',
            'address': 'Адреса доставки',
            'notes': 'Коментар',
        }
