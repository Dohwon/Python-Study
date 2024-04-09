def make_juice(fruit):
  #if fruit == "과일을 넣어주세요":
  #  again_fruit = input("과일을 넣어주세요: ")
  #  make_juice(again_fruit)
  #else:
  return f"{fruit}+🥤"

def add_ice(juice="먼저 주스를 만들어주세요"):
  if juice == "먼저 주스를 만들어주세요":
    print("먼저 주스를 만들어주세요:")
    make_juice()
  else:
    return f"{juice}+🧊"

def add_sugar(ice_juice="먼저 주스를 만들고, 얼음을 넣어주세요."):
  if ice_juice == "먼저 주스를 만들고, 얼음을 넣어주세요.":
    input("먼저 주스를 만들고, 얼음을 넣어주세요.")
    make_juice()
  else:
    return f"{ice_juice}+🍬"



def perfect_juice(fruit="과일을 넣어주세요"):
  if fruit == "과일을 넣어주세요":
    again_fruit = input("과일을 넣어주세요: ")
    juice = make_juice(again_fruit)
    iced_juice = add_ice(juice)
    perfect_juice = add_sugar(iced_juice)
    print(perfect_juice)
  else:
    juice = make_juice(fruit)
    iced_juice = add_ice(juice)
    perfect_juice = add_sugar(iced_juice)
    print(perfect_juice)

print(perfect_juice())
print(perfect_juice("🍎"))