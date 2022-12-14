from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView, Request, Response, status

from transactions.models import Transaction
from utils.handle_txt import transaction_list, transaction_sum


# Create your views here.
def upload(request: Request):
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        transactions = transaction_list(f"upload/{uploaded_file}")

        for transaction in transactions:
            Transaction.objects.create(**transaction)

        return redirect("/page/transactions/")
    return render(request, "upload.html")


def transactions_view(request):
    transactions = Transaction.objects.values(
        "type",
        "date",
        "value",
        "cpf",
        "card",
        "hour",
        "shop_owner",
        "shop_name",
    )

    sum = transaction_sum(transactions)

    return render(
        request,
        "transactions.html",
        context={
            "transactions": transactions,
            "sum": sum,
        },
    )
