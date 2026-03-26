lst = ["a", "aba", "asd", "sdsds", "akdfhakhf", "asasa"]

def f(x):
    return len(x)

print(sorted(lst, key=f))