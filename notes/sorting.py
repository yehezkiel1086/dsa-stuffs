def bubble_sort(arr):
    return arr

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [7, 12, 9, 11, 3]
    # s_arr = insertion_sort(arr)
    s_arr = bubble_sort(arr)
    
    print(s_arr)