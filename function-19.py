def string(s):
    if s == "":
        return 0
    return 1 + string(s[1:])

text = "hello"
print("Length:", string(text))
