if __name__ == '__main__':
    s = input()
    
    has_alnum = False
    has_chara = False
    has_digit = False
    has_lower = False
    has_upper = False
    
    for x in s:
        if x.isalnum():
            has_alnum = True
        if x.isalpha():
            has_chara = True
        if x.isdigit():
            has_digit = True
        if x.islower():
            has_lower = True
        if x.isupper():
            has_upper = True
    
    if has_alnum:
        print("True")
    else:
        print("False")
    if has_chara:
        print("True")
    else:
        print("False")
    if has_digit:
        print("True")
    else:
        print("False")
    if has_lower:
        print("True")
    else:
        print("False")
    if has_upper:
        print("True")
    else:
        print("False")