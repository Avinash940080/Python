def divide(a, b):
  return a / b

try:
  a = int(input("Enter a: "))
  b = int(input("Enter b: "))
  print("After division: ", divide(a, b))

except IndexError:
  print("Index error")

except ZeroDivisionError:
  print("Zero division error")