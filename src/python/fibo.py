firstElement = 0
secondElement = 1
count = 0
result = firstElement + secondElement
fiboNumber = input("input fibo number:")

while count < fiboNumber:
  thirdElement = firstElement + secondElement
  result += thirdElement
  firstElement = secondElement
  secondElement = thirdElement
  count += 1
print("fibo result is {} and calculation result is {}".format(thirdElement, result))
