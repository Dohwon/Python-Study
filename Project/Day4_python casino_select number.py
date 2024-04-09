"""from random import randint

user_choice = int(input("Choose number: "))
pc_choice = randint(1,50) #I imported this

if user_choice == pc_choice:
  print("You win!")
elif user_choice > pc_choice:
  print("Lower! Computer choose", pc_choice)
else:
  print("Higher! Computer choose", pc_choice)
"""

from random import randint

print("Welcome to Python Casino")

pc_choice = randint(1,50)

playing = True
count = 0

while playing:
  user_choice = int(input("Choose number: "))
  if user_choice == pc_choice:
    print(f"befor than {count+1}, You win!")
    break
  elif user_choice > pc_choice:
    print("Lower! Computer choose")
  else:
    print("Higher! Computer choose")
  count = count + 1
  if count < 5:
    continue
  else: 
    print("You lose!")
    break  