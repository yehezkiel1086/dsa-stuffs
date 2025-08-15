import textwrap

def wrap(string, max_width):
    arr = []
    tmp = ""
    for i, x in enumerate(string):
        tmp += x
        if (i + 1) % max_width == 0:
            arr.append(tmp)
            tmp = ""
    if len(tmp) != 0:
        arr.append(tmp)
    return "\n".join(arr)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)