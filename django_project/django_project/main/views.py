from django.shortcuts import redirect, render

from .forms import CalculatorForm, OrderForm, StudentForm


PRODUCT_PRICES = {
    "laptop": 5_000_000,
    "phone": 3_000_000,
    "headphones": 200_000,
}
DELIVERY_FEES = {"pickup": 0, "courier": 30_000}
OPERATION_SYMBOLS = {
    "add": "+",
    "subtract": "−",
    "multiply": "×",
    "divide": "÷",
}


def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            request.session["student_result"] = form.cleaned_data
            return redirect("student_result")
    else:
        form = StudentForm()
    return render(request, "main/student.html", {"form": form})


def student_result(request):
    data = request.session.pop("student_result", None)
    if data is None:
        return redirect("student")
    return render(request, "main/student_result.html", {"student": data})


def calculator(request):
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data["first_number"]
            second = form.cleaned_data["second_number"]
            operation = form.cleaned_data["operation"]
            if operation == "add":
                result = first + second
            elif operation == "subtract":
                result = first - second
            elif operation == "multiply":
                result = first * second
            else:
                result = first / second

            request.session["calculator_result"] = {
                "first": format(first, "g"),
                "second": format(second, "g"),
                "symbol": OPERATION_SYMBOLS[operation],
                "result": format(result, "g"),
            }
            return redirect("calculator_result")
    else:
        form = CalculatorForm()
    return render(request, "main/calculator.html", {"form": form})


def calculator_result(request):
    data = request.session.pop("calculator_result", None)
    if data is None:
        return redirect("calculator")
    return render(request, "main/calculator_result.html", {"calculation": data})


def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product_label = dict(OrderForm.PRODUCT_CHOICES)[data["product"]].split(" — ")[0]
            delivery_label = dict(OrderForm.DELIVERY_CHOICES)[data["delivery"]].split(" — ")[0]
            unit_price = PRODUCT_PRICES[data["product"]]
            delivery_fee = DELIVERY_FEES[data["delivery"]]
            total = unit_price * data["quantity"] + delivery_fee

            request.session["order_result"] = {
                "customer_name": data["customer_name"],
                "phone": data["phone"],
                "product": product_label,
                "quantity": data["quantity"],
                "unit_price": f"{unit_price:,}".replace(",", " "),
                "delivery": delivery_label,
                "address": data["address"],
                "total": f"{total:,}".replace(",", " "),
            }
            return redirect("order_result")
    else:
        form = OrderForm()
    return render(request, "main/order.html", {"form": form})


def order_result(request):
    data = request.session.pop("order_result", None)
    if data is None:
        return redirect("order")
    return render(request, "main/order_result.html", {"order": data})
