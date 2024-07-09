import math
from collections import Counter

def calculate_mean(data):
    mean_value = sum(data) / len(data)
    return mean_value

def calculate_variance(data):
    mean_value = calculate_mean(data)
    squared_differences = [(x - mean_value) ** 2 for x in data]
    variance = sum(squared_differences) / len(data)
    return variance

def calculate_standard_deviation(data):
    variance = calculate_variance(data)
    return math.sqrt(variance)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle = n // 2
    
    if n % 2 == 0:
        median_value = (sorted_data[middle - 1] + sorted_data[middle]) / 2
    else:
        median_value = sorted_data[middle]
    
    return median_value

def calculate_mode(data):
    data_count = Counter(data)
    max_count = max(data_count.values())
    mode_values = [k for k, v in data_count.items() if v == max_count]
    
    if len(mode_values) == len(data):
        return None
    
    return mode_values

def calculate_coefficient_of_variation(data):
    mean_value = calculate_mean(data)
    standard_deviation = calculate_standard_deviation(data)
    if mean_value == 0:
        return float('inf')
    cv = standard_deviation / mean_value
    return cv * 100

input_data = input("Masukkan data (pisahkan dengan koma): ")
data = list(map(int, input_data.split(',')))

mean_value = calculate_mean(data)
median_value = calculate_median(data)
mode_values = calculate_mode(data)
variance = calculate_variance(data)
standard_deviation = calculate_standard_deviation(data)
coefficient_of_variation = calculate_coefficient_of_variation(data)

print("Mean:", mean_value)
print("Median:", median_value)
if mode_values:
    print("Modus:", mode_values)
else:
    print("Modus: Tidak ada modus (semua nilai unik)")
print("Variansi:", variance)
print("Standar Deviasi:", standard_deviation)
print(f"Koefisien Variansi: {coefficient_of_variation:.2f}%")
