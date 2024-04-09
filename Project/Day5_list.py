#days_of_week = ["Mon", "Tue", "wed", "Thu", "Fri"]

"""name = "dowon"

print(name.upper())
print(name.capitalize())
print(name.lower())
print(name.isupper())
print(name.islower())
print(name.istitle())
print(name.isdigit())
print(name.isalpha())
print(name.isalnum())
print(name.isspace())
print(name.isprintable())
print(name.isascii())
"""

""
# value값을 None으로 두는 방법?
player = [{
  'name' : 'nico',
  'age' : 12,
  'alive' : True,
  'fav_food' : None},
          {
            'name' : 'dowon',
            'age' : 29,
            'alive' : True,
            'fav_food' : None}]

print(player) #먼저 만든 리스트 출력

print(player[1].get('age')) #player의 두번째 요소의 age 출력

#player의 모든 'name' key의 value를 리스트로 출
name = []
print(len(player))

for i in (0, len(player)-1):
  a = player[i].get('name')
  name.append(a)
print(name)


#player에 'fav_food' key, value 최초 변경
player[0]['fav_food'] = "pizza"
player[1]['fav_food'] = "burger"
print(player)

#player에 'fav_food' key, value 추가하려면 list형태여야 함. 따라서 아래 코드는 실행안
"""
player[0]['fav_food'].append(('pasta'))
player[1]['fav_food'].append(('chicken'))
print(player)
"""

# 아래 두개는 같은 표현 방법
print(player[1].get('fav_food'))
print(player[1]['fav_food'])


player = ['nico', 'dowon']
print(player[0])
# 이건 안됨 print(player["nico"])