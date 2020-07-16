def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s
mystr =input("Enter a string : ")
print("Reversed String: ", reverse(mystr))