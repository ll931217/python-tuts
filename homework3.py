def checkNumbers(a, b, c):
  if int(a) == int(b) or int(b) == int(c) or int(c) == int(a):
    return True
  else:
    return False

print(checkNumbers(6, 5, "5"))
