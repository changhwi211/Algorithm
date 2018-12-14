def palindrome(str):
    for i in str:
        if str.isalpha():
            break
        if not i.isalpha():
            str = str.replace(i, "")
            
    for i in range(len(str)//2):
        if str[i].lower() != str[-(i+1)].lower():
            return False
    return True

print(palindrome("ab/cba##"))

print(palindrome("ac/cba##"))