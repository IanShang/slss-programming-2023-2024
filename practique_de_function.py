def stars(l: int) -> str:
    pyramid = ""
    for n in range(1, l+1):
        if (n<l):
            pyramid += "*" * n + "\n"
        else: pyramid += "*" * n
    return pyramid
print(stars(6))