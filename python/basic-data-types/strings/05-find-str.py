def count_substring(string, sub_string):
    tt = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        s = string[i : i+len(sub_string)]
        
        if s == sub_string:
            tt += 1
    
    return tt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)