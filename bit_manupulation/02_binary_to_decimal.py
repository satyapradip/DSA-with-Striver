def convert2Decimal(x:str)->int:
  decimal_num = 0
  power = 0
  index = len(x) - 1
  while index >= 0:
    num = int(x[index]) * (2**power)
    decimal_num += num
    index -= 1
    power += 1
  return decimal_num

if __name__ == "__main__":
  print(convert2Decimal("0101"))