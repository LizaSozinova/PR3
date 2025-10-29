from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

balance = 0

def status(request):
    return JsonResponse({"status": "ok"})

@csrf_exempt
def add(request):
    global balance
    kind = request.GET.get("kind")
    amount = float(request.GET.get("amount", 0))
    if kind == "income":
        balance += amount
    elif kind == "expense":
        balance -= amount
    return JsonResponse({"balance": balance})

def get_balance(request):
    return JsonResponse({"balance": balance})
