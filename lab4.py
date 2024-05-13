def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

alphabet_array = ['z', 'a', 'b', 'h', 'c', 'f', 'd', 'e']


bubble_sort(alphabet_array)

print("Sorted Array:", alphabet_array)
