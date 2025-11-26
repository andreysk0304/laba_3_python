from src.functions.factorial import factorial
from src.functions.fibonacci import fibonacci
from src.functions.sorts.bubble_sort import bubble_sort
from src.functions.sorts.bucket_sort import bucket_sort
from src.functions.sorts.counting_sort import counting_sort
from src.functions.sorts.heap_sort import heap_sort
from src.functions.sorts.quick_sort import quick_sort
from src.functions.sorts.radix_sort import radix_sort

SORTES = {
    'quick_sort': {'func': quick_sort, 'type': 'int'},
    'bubble_sort': {'func': bubble_sort, 'type': 'int'},
    'bucket_sort': {'func': bucket_sort, 'type': 'float'},
    'counting_sort': {'func': counting_sort, 'type': 'int'},
    'heap_sort': {'func': heap_sort, 'type': 'int'},
    'radix_sort': {'func': radix_sort, 'type': 'int'},
}

ALGOS = {
    'fib': fibonacci,
    'factorial': factorial
}

STACK = ['push', 'pop', 'peek', 'min', 'is_empty']
QUEUE = ['enqueue', 'dequeue', 'front', 'is_empty']

COMMANDS = (
    'Все команды:\n\n'
    
    'ВАЖНО: если не указать список, который будет сортировать функция, то будет использоваться рандомно сгенерированный список, его можно посмотреть командой lists!\n\n'
    
    'quick_sort ( допускается флаг -b, можно передать свой список в формате "1,3,2,45,6", пример: quick_sort -b 1,2,3,4,5)\n'
    'bubble_sort ( допускается флаг -b )\n'
    'bucket_sort ( допускается флаг -b )\n'
    'counting_sort ( допускается флаг -b )\n'
    'heap_sort ( допускается флаг -b )\n'
    'radix_sort ( допускается флаг -b )\n\n'
    
    'stack - отобразит удобную подсказку о работе с ним\n'
    'queue - отобразит удобную подсказку о работе с ним\n\n'
    
    'lists - отображает рандомно сгенерированные списки\n'
    'rc - перегенерирует списки для тестов\n\n' 
    'stop - прекращает исполнения cli приложения "Андрюшка"\n'
    'help - показывает все команды ( и да, вы сейчас здесь ;D )'
)