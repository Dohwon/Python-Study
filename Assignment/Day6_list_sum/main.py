numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]

plus_number = []

for number in numbers:
  if type(number) == int:
    plus_number.append(number)
print(sum(plus_number))


# solution nico
"""
final = 0  # 그냥 0이라고 해도 됨. 변수 선언만

for number in numbers:
  if type(number) is int: final += item
  # ==는 is로 써도 되고, append 대신에 +=로 해도 됨.
  # 순서 주의 final에 item을 추가하는거니까 final += item
"""