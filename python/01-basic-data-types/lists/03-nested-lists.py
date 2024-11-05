if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    min_v = min(arr, key=lambda x: x[1])[1]
    sec_min_v = sorted([x for _, x in arr if x > min_v])[0]
    result = sorted([x for x, y in arr if y == sec_min_v])
    print("\n".join(result))