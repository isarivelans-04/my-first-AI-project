value = int(input())

try:
    print(float(value) * 10)   # works if it's a number
except ValueError:
    print(value * 10)          # otherwise repeat the text