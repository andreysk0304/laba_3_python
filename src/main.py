from src.functions.factorial import *
from src.functions.fibonacci import *
from src.functions.sorts.bubble_sort import *
from src.functions.sorts.heap_sort import heap_sort
from src.functions.sorts.quick_sort import *
from src.functions.sorts.bucket_sort import *


def main() -> None:
    print(factorial_recursive(10))
    print(factorial(10))

    print(fibonacci_recursive(10))
    print(fibonacci(10))

    print(sorted([2, 3, 4, 1, 7]))
    print(bubble_sort([2, 3, 4, 1, 7]))
    print(quick_sort([2, 3, 4, 1, 7]))
    print(heap_sort([2, 3, 4, 1, 7]))

    print(bucket_sort([0.23, 0.12, 0.94, 0.3923, 0.328328, 0.09, 0.103, 0.3]))

if __name__ == "__main__":
    main()
