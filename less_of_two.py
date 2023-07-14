def myfunc(a,b):
  if a % 2 == 0 and b % 2 == 0:
  # BOTH NUMBERS ARE EVEN
    if a < b:
      result = a
    else:
      result = b
  else:
  # ONE OR BOTH NUMBERS ARE ODD
    if a > b:
      result = a
    else:
      result = b

  return result


print(myfunc(2,4)) # output = 2

print(myfunc(2,5)) # output = 5