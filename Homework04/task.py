import math


def pearson_correlation(arr_1, arr_2):
   
    """
    Расчет корреляции Пирсона между двумя массивами.

    Args:
     - arr_1: первый массив значений
     - arr_2: второй массив значений

    Return:
     - Корреляция Пирсона между массивами arr_1 и arr_2
    """

    # Проверка на то, что массивы одинаковой длины
    if len(arr_1) != len(arr_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(arr_1)

    # Расчет среднего значения
    mean_x = sum(arr_1) / n
    mean_y = sum(arr_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in arr_1]) / float(len(arr_1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in arr_2]) / float(len(arr_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(arr_1,arr_2)]) / float(len(arr_1)) 
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation

arr_1 = [1,2,3,4,5,7,77]
arr_2 = [6,7,8,9,5,6,7]

correlation = round(pearson_correlation(arr_1, arr_2),4)
print(f"Корреляция Пирсона: {correlation}")