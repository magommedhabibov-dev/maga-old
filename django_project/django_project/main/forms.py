from django import forms


class StudentForm(forms.Form):
    first_name = forms.CharField(label="Имя", max_length=100)
    last_name = forms.CharField(label="Фамилия", max_length=100)
    age = forms.IntegerField(label="Возраст")
    email = forms.EmailField(label="Email")


class CalculatorForm(forms.Form):
    OPERATION_CHOICES = (
        ("add", "Сложение (+)"),
        ("subtract", "Вычитание (−)"),
        ("multiply", "Умножение (×)"),
        ("divide", "Деление (÷)"),
    )

    first_number = forms.FloatField(label="Первое число")
    second_number = forms.FloatField(label="Второе число")
    operation = forms.ChoiceField(label="Операция", choices=OPERATION_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        if (
            cleaned_data.get("operation") == "divide"
            and cleaned_data.get("second_number") == 0
        ):
            self.add_error("second_number", "На ноль делить нельзя.")
        return cleaned_data


class OrderForm(forms.Form):
    PRODUCT_CHOICES = (
        ("laptop", "Ноутбук — 5 000 000 сум"),
        ("phone", "Телефон — 3 000 000 сум"),
        ("headphones", "Наушники — 200 000 сум"),
    )
    DELIVERY_CHOICES = (
        ("pickup", "Самовывоз — бесплатно"),
        ("courier", "Курьер — 30 000 сум"),
    )

    customer_name = forms.CharField(label="Имя покупателя", max_length=100)
    phone = forms.CharField(label="Телефон", max_length=30)
    product = forms.ChoiceField(label="Товар", choices=PRODUCT_CHOICES)
    quantity = forms.IntegerField(label="Количество", min_value=1)
    delivery = forms.ChoiceField(label="Доставка", choices=DELIVERY_CHOICES)
    address = forms.CharField(label="Адрес", max_length=255)
