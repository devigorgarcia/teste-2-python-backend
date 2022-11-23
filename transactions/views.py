from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

from transactions.models import Transaction
from utils.handle_txt import transaction_list


# Create your views here.
def upload(request: Request):
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        transactions = transaction_list(f"upload/{uploaded_file}")

        for transaction in transactions:
            content = Transaction.objects.create(**transaction)

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

    return render(request, "transactions.html", context={"transactions": transactions})
