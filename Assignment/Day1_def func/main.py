def tax_cal(money):
  return money*0.35

def pay(tax):
  print("Thank you for paying", tax)


to_pay = tax_cal(150)
pay(to_pay)
pay(tax_cal(150))