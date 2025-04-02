
from django.shortcuts import render
from .algorithms import ordenamientoBurbuja, busquedaBinaria, maximoComunDivisor 

def index(request):
    result = None
    if request.method == 'POST':
        algorithm = request.POST.get('algorithm')
        
        if algorithm == 'ordenamientoBurbuja':
            input_data = request.POST.get('input_data')
            arr = list(map(int, input_data.split(',')))
            result = ordenamientoBurbuja(arr)
        
        elif algorithm == 'busquedaBinaria':
            input_data = request.POST.get('input_data')
            target = int(request.POST.get('target'))
            arr = list(map(int, input_data.split(',')))
            arr_sorted = sorted(arr)
            result = busquedaBinaria(arr_sorted, target)
        
        elif algorithm == 'maximoComunDivisor':
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            result = maximoComunDivisor(num1, num2)
    
    return render(request, 'algoritmos/index.html', {'result': result})